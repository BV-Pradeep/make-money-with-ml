from django.db import models

# Create your models here.


class LoanApproval(models.Model):
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=10, choices=(('Male','Male'),('Female','Female')))
	Married=models.CharField(max_length=10, choices=(('Yes','Yes'),('No','No')))
	Dependents=models.CharField(max_length=2, choices=(('1','1'),('2','2'),('3+','3+')))
	Education=models.CharField(max_length=20, choices=(('Graduate','Graduate'),('Not Graduate','Not Graduate')))
	Self_Employed=models.CharField(max_length=5,choices=(('Yes','Yes'),('No','No')))
	ApplicantIncome=models.IntegerField()
	CoapplicantIncome=models.IntegerField()
	LoanAmount=models.IntegerField()
	Loan_Amount_Term=models.IntegerField()
	Credit_History=models.FloatField(choices=((1.0,'Yes'),(0.0,'No')))
	Property_Area=models.CharField(max_length=10,choices=(('Urban','Urban'),('Rural','Rural'),('Semiurban','Semiurban')))

	def __str__(self):
		return self.Name

