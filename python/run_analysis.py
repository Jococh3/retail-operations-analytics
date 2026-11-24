from pathlib import Path
import sqlite3, pandas as pd, numpy as np, json
from scipy.stats import mannwhitneyu
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]; out=root/'results'; processed=root/'data/processed'; out.mkdir(exist_ok=True); processed.mkdir(exist_ok=True)
db=processed/'olist.sqlite'; db.unlink(missing_ok=True); con=sqlite3.connect(db); frames={}
for f in sorted((root/'data/raw').glob('*.csv')):
    name=f.stem.replace('olist_','').replace('_dataset',''); d=pd.read_csv(f); d.to_sql(name,con,index=False); frames[name]=d
for t,k in [('orders','order_id'),('customers','customer_id'),('order_items','order_id'),('order_reviews','order_id'),('products','product_id'),('sellers','seller_id')]: con.execute(f'CREATE INDEX idx_{t} ON {t}({k})')
con.executescript((root/'sql/views.sql').read_text())
for f in sorted((root/'sql').glob('q*.sql')): pd.read_sql_query(f.read_text(),con).to_csv(out/(f.stem+'.csv'),index=False)
f=pd.read_sql_query('SELECT * FROM order_fact',con); i=pd.read_sql_query('SELECT * FROM item_fact',con); f.to_csv(processed/'order_fact.csv',index=False); i.to_csv(processed/'item_fact.csv',index=False)
o=frames['orders']; raw=frames['order_items']; eligible=o.order_delivered_customer_date.notna() & o.order_estimated_delivery_date.notna(); late=pd.to_datetime(o.loc[eligible,'order_delivered_customer_date']).dt.normalize()>pd.to_datetime(o.loc[eligible,'order_estimated_delivery_date']).dt.normalize(); duration=(pd.to_datetime(o.loc[eligible,'order_delivered_customer_date'])-pd.to_datetime(o.loc[eligible,'order_purchase_timestamp'])).dt.total_seconds()/86400
checks={'unique_orders':bool(f.order_id.is_unique),'orders':len(f)==len(o),'items':len(i)==len(raw),'revenue':bool(np.isclose(f.revenue.sum(),raw.price.sum())),'freight':bool(np.isclose(f.freight.sum(),raw.freight_value.sum())),'eligible':int(f.eligible.sum())==int(eligible.sum()),'late':int(f.late.sum())==int(late.sum()),'duration':bool(np.isclose(f.loc[f.eligible==1,'delivery_days'].mean(),duration.mean()))}; assert all(checks.values()),checks
a=f.loc[f.late==0,'review_score'].dropna(); b=f.loc[f.late==1,'review_score'].dropna(); u,p=mannwhitneyu(a,b); summary=dict(orders=len(f),items=len(i),revenue=float(f.revenue.sum()),freight=float(f.freight.sum()),eligible=int(eligible.sum()),late=int(late.sum()),late_rate=float(late.mean()),mean_days=float(duration.mean()),on_time_review=float(a.mean()),late_review=float(b.mean()),on_time_n=len(a),late_n=len(b),mann_whitney_u=float(u),p_value=float(p),checks=checks); (out/'validation.json').write_text(json.dumps(summary,indent=2)); print(summary)
for name,x,y,title in [('q02_monthly','month','revenue','Monthly merchandise revenue (BRL)'),('q03_state','state','late_rate','Late delivery rate by state'),('q07_reviews','delivery_group','mean_review','Average review score by delivery group')]:
    d=pd.read_csv(out/(name+'.csv')); fig,ax=plt.subplots(figsize=(10,5)); ax.bar(d[x],d[y]); ax.set_title(title); ax.tick_params(axis='x',rotation=65); fig.tight_layout(); fig.savefig(out/(name+'.png'),dpi=150); plt.close(fig)
con.close()
