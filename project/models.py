from django.db import models
from simple_history.models import HistoricalRecords

'''
MODELS.PY DEFINES THE DATABASE OBJECTS AND HOW THEY ARE STORED. CREATING MODELS FOR VARIABLES LIKE "COMPUTE SIZE"
ALLOWS USERS TO ENTER MORE DROPDOWN OPTIONS ON THE ADMIN SITE BUT DECREASES PERFORMANCE (MORE UNNECESSARY DB QUERIES). 
BE SURE TO RUN "$ py manage.py makemigrations" AND "$ py manage.py migrate" WHENEVER YOU MAKE CHANGES TO MODELS.PY AS
THIS WILL UPDATE THE DATABASE
'''

class Site(models.Model):
	site_choices = (
		('SAN', 'SAN'), 
		('BLR', 'BLR',),
		)
	site = models.CharField(max_length = 20, choices = site_choices)
	project = models.ForeignKey('Project', null = True, blank = True)
	#foreign key relationship between site and project. allows users to filter projects by site and build more
	#meaningful database connections. including "null=True, blank=True" allows you to add more variables even if 
	#there is previous data without those variables

	def __str__(self):
	#how the model will be represented in the database
		return self.site

class Function(models.Model):
	function_choices = (
		('PD', 'PD'),
		('DFT', 'DFT'),
		('PTE', 'PTE'),
		)
	function = models.CharField(max_length = 20, choices = function_choices)
	site = models.ForeignKey('Site', null=True, blank=True)

	def __str__(self):
		return self.function

class SlotsOrHosts(models.Model):
	#these class-based models simply define the variables. users must go into the admin and populate them
	#the first time they use the app or if the database is cleared
	slots_or_hosts = models.CharField(max_length = 10)

	def __str__(self):
		return self.slots_or_hosts

class ComputeSize(models.Model):
	compute_size = models.CharField(max_length = 10)

	def __str__(self):
		return self.compute_size

class StorageTier(models.Model):
	storage_tier = models.CharField(max_length = 10) 

	def __str__(self):
		return self.storage_tier

class StorageSize(models.Model):
	storage_size = models.CharField(max_length = 15)

	def __str__(self):
		return self.storage_size

class Cluster(models.Model):
	cluster = models.CharField(max_length = 20) 

	def __str__(self):
		return self.cluster

class Island(models.Model):
	island = models.CharField(max_length = 20) 

	def __str__(self):
		return self.island

class ComputeProfile(models.Model):
	#a project's compute profile is the compute information for a range of months. it includes 
	#foreign key relationsips to the cluster, slots/hosts, compute size, and function, which allows 
	#admins to populate those dropdown boxes while on the 'create project' form
	cluster = models.ForeignKey('Cluster', null = True, blank = True)
	slots_or_hosts = models.ForeignKey('SlotsOrHosts', null = True, blank = True)
	compute_size = models.ForeignKey('ComputeSize', null = True, blank = True)
	function = models.ForeignKey('Function', null = True, blank = True) 

	#months are currently hardcoded. this should change
	compute_jan = models.CharField(verbose_name = "January-17", max_length = 10, default = 0,)
	compute_feb = models.CharField(verbose_name = "February-17", max_length = 10, default = 0,)
	compute_mar = models.CharField(verbose_name = "March-17", max_length = 10, default = 0,)
	compute_apr = models.CharField(verbose_name = "April-17", max_length = 10, default = 0,)
	compute_may = models.CharField(verbose_name = "May-17", max_length = 10, default = 0,)
	compute_jun = models.CharField(verbose_name = "June-17", max_length = 10, default = 0,)
	compute_jul = models.CharField(verbose_name = "July-17", max_length = 10, default = 0,)
	compute_aug = models.CharField(verbose_name = "August-17", max_length = 10, default = 0,)
	compute_sep = models.CharField(verbose_name = "September-17", max_length = 10, default = 0,)
	compute_oct = models.CharField(verbose_name = "October-17", max_length = 10, default = 0,)
	compute_nov = models.CharField(verbose_name = "November-17", max_length = 10, default = 0,)
	compute_dec = models.CharField(verbose_name = "December-17", max_length = 10, default = 0,)
    
    #version control package. allows 'history' functionality and lets admins see who has made changes
    #to a project and what those changes were
	history = HistoricalRecords()

	def __str__(self):
		#how a project's compute profile is represented in the database
		return "{}--{}".format(self.slots_or_hosts, self.compute_size)

class StorageProfile(models.Model):
	#similar to above, but with foreign key relationships to island, storage tier, storage size, and 
	#function
	island = models.ForeignKey('Island', null = True, blank = True)
	storage_tier = models.ForeignKey('StorageTier', null = True, blank = True)
	storage_size = models.ForeignKey('StorageSize', null = True, blank = True)
	function = models.ForeignKey('Function', null = True, blank = True)

	#as above, the forecasting schedule is currently hardcoded. this should change. ideally users
	#will be able to choose a start and end month and then have the table automatically create fields 
	#for that range of months. remove "default = 0" if you want to start with blank fields
	storage_jan = models.CharField(verbose_name = "January-17", max_length = 10, default = 0,)
	storage_feb = models.CharField(verbose_name = "February-17", max_length = 10, default = 0,)
	storage_mar = models.CharField(verbose_name = "March-17", max_length = 10, default = 0,)
	storage_apr = models.CharField(verbose_name = "April-17", max_length = 10, default = 0,)
	storage_may = models.CharField(verbose_name = "May-17", max_length = 10, default = 0,)
	storage_jun = models.CharField(verbose_name = "June-17", max_length = 10, default = 0,)
	storage_jul = models.CharField(verbose_name = "July-17", max_length = 10, default = 0,)
	storage_aug = models.CharField(verbose_name = "August-17", max_length = 10, default = 0,)
	storage_sep = models.CharField(verbose_name = "September-17", max_length = 10, default = 0,)
	storage_oct = models.CharField(verbose_name = "October-17", max_length = 10, default = 0,)
	storage_nov = models.CharField(verbose_name = "November-17", max_length = 10, default = 0,)
	storage_dec = models.CharField(verbose_name = "December-17", max_length = 10, default = 0,)

	#version control package
	history = HistoricalRecords()

	def __str__(self):
		#how a project's storage profile is represented in the database
		return "{}--{}".format(self.storage_tier, self.storage_size)

class Project(models.Model):
	#the details of a project that aren't storage/compute information
	project_created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
	project_name = models.CharField(verbose_name = "Name", max_length = 20)
	project_version = models.CharField(verbose_name = "Version", max_length=5, choices = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9)])
	project_class = models.CharField(verbose_name = "Class", max_length = 30)
	project_contact_primary = models.CharField(verbose_name = "Primary Contact", max_length = 30)
	project_contact_secondary = models.CharField(verbose_name = "Secondary Contact", null = True, blank = True, max_length = 30, default = 'None')

	#version control package
	history = HistoricalRecords()

	def __str__(self):
		#how a project is represented in the database
		return "{}--{}".format(self.project_name, self.project_version)


