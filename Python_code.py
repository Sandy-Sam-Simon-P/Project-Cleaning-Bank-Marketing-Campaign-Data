import pandas as pd
import numpy as np

# Start coding here...
data = pd.read_csv('bank_marketing.csv')
data = pd.DataFrame(data)
print(data.isna().any())

#Client data
client = data[['client_id','age','job','marital','education','credit_default','mortgage']]
client['job'] = client['job'].str.replace('.','_')
client['education'] = client['education'].str.replace('.','_')
client['education'] = client['education'].replace('unknown',np.NaN)
client['credit_default'] = client['credit_default'].astype(bool)
client['mortgage'] = client['mortgage'].astype(bool)
client.to_csv('client.csv',index = False)

#Campaign Data
campaign = data[["client_id", "number_contacts", "month", "day","contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]]
campaign['previous_outcome'] = campaign['previous_outcome'].astype(bool)
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype(bool)
campaign['day'] = campaign['day'].astype(str)
campaign['month'] = campaign['month'].str.capitalize()
campaign['year'] = '2022'
campaign['last_contact_date'] = campaign['year']+"-"+campaign['month']+"-"+campaign['day']
campaign['last_contact_date'] = pd.to_datetime(campaign["last_contact_date"], format="%Y-%b-%d")
campaign.drop(columns=["month", "day", "year"], inplace=True)
campaign.to_csv('campaign.csv',index = False)

#economics Data
economics = data[['client_id','cons_price_idx','euribor_three_months']]
economics.to_csv('economics.csv',index = False)
