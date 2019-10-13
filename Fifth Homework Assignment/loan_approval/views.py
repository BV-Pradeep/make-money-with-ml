from django.shortcuts import render,redirect
import razorpay
import json
from .forms import LoanForm
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, Normalizer,StandardScaler
from sklearn.externals import joblib
import numpy as np

def acceptpayments(request):
	razorpay_client = razorpay.Client(auth=("rzp_test_HNcMCOUHPcHzn3", "kTIqOIRrWsa989G9LRpprMyA"))
	template_name='payment_form.html'

	if request.method=='POST':
		#chargeapp()
		return redirect('loan:predict')
	else:
		return render(request,template_name,{})

def chargeapp():
    amount = 5100
    payment_id = request.form['razorpay_payment_id']
    razorpay_client.payment.capture(payment_id, amount)
    return json.dumps(razorpay_client.payment.fetch(payment_id))


def loanform(request):
	answer=0
	template_name='loan_form.html'
	if request.method=='POST':
		loan_form=LoanForm(request.POST)
		if loan_form.is_valid():
			Name=loan_form.cleaned_data['Name']
			Gender=loan_form.cleaned_data['Gender']
			Married=loan_form.cleaned_data['Married']
			Dependents=loan_form.cleaned_data['Dependents']
			Education=loan_form.cleaned_data['Education']
			Self_Employed=loan_form.cleaned_data['Self_Employed']
			ApplicantIncome=loan_form.cleaned_data['ApplicantIncome']
			CoapplicantIncome=loan_form.cleaned_data['CoapplicantIncome']
			LoanAmount=loan_form.cleaned_data['LoanAmount']
			Loan_Amount_Term=loan_form.cleaned_data['Loan_Amount_Term']
			
			Credit_History=loan_form.cleaned_data['Credit_History']

			#Credit_History=float(Credit_History1)
			Property_Area=loan_form.cleaned_data['Property_Area']

			loan_form.save()
			MyDict= (request.POST).dict()
			data=pd.DataFrame(MyDict,index=[0])
			#print(data)
			answer=get_answer(ohevalue(data))
			if(answer>0.5):
				return redirect('loan:approved')
			else:
				return redirect('loan:rejected')
			
	else:
		loan_form=LoanForm(request.POST)



	return render(request,template_name,{'loan_form':loan_form,'answer':answer})


def get_answer(data):
	scaler = joblib.load('D:/Raj/make money with ml/5th week/env/src/scaler.save')
	data_scaled=scaler.transform(data)
	#data_scaled = sc.fit_transform(data.reshape(20,-1))
	#data_test = data_scaled.reshape( -1, 20)
	mdl=joblib.load('D:/Raj/make money with ml/5th week/env/src/loan_model.pkl')
	y_pred=mdl.predict(data_scaled)
	print(data_scaled)
	print(y_pred)
	return y_pred[0]


def ohevalue(data):
	data=data.drop(['Name','csrfmiddlewaretoken'],axis=1)
	ohe_columns=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
	'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male',
	'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1',
	'Dependents_2', 'Dependents_3+', 'Education_Graduate',
	'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
	'Property_Area_Rural', 'Property_Area_Semiurban','Property_Area_Urban']

	cat_columns=['Gender','Dependents','Education','Self_Employed','Property_Area','Married']

	new_dict={}
	data_processed=pd.get_dummies(data, columns=cat_columns)

	for i in ohe_columns:
		if i in data_processed.columns:
			new_dict[i]=data_processed[i].values
		else:
			new_dict[i]=0

	newdf=pd.DataFrame(new_dict)
	print(newdf['Credit_History'])
	return newdf

def loan_approved(request):
	template_name='approved.html'

	return render(request,template_name)

def loan_rejected(request):
	template_name='rejected.html'
	return render(request,template_name)
