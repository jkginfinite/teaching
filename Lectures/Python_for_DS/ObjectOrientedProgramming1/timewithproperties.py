"""Class with time read-write properties"""
from datetime import datetime,timedelta

class Time:
	"""Class time with read-write properties"""
	def __init__(self,hour = 0,minute = 0,second = 0):
		"""Initialize each attrbiute"""
		self.hour = int(hour)
		self.minute = int(minute)
		self.second = int(second)
		self.time = (self.hour,self.minute,self.second)

	@property
	def hour(self):
		"""Return the hour"""
		return self._hour

	@hour.setter
	def hour(self,hour):
		"""Set the hour."""
		if not (0<=hour<24):
			raise ValueError(f'Hour ({hour}) must be 0-23')
		self._hour = hour

	@property
	def minute(self):
		"""Return the minute"""
		return self._minute

	@minute.setter
	def minute(self,minute):
		"""Set minute"""
		if not (0<=minute<60):
			raise ValueError(f'Minute({minute}) must be 0-59')
		self._minute = minute

	@property
	def second(self):
		"""Return the second"""
		return self._second


	@second.setter
	def second(self,second):
		""" Set the second"""
		if not (0<=second<60):
			raise ValueError(f'Second ({second}) must be 0-59')
		self._second = second


	def set_time(self,hour=0,minute=0,second=0):
		"""set values of hour, minute and second"""
		self.hour = hour
		self.minute = minute
		self.second = second
		self._time  = (hour,minute,second)


	@property
	def time(self):
		"""Return hour, minute and second as a tuple"""
		return self._time

	@time.setter
	def time(self,time_tuple):
		"""Set time form a tuple comntianing hour,minute and second"""
		self.set_time(time_tuple[0],time_tuple[1],time_tuple[2])
	

	def add_time(self,hour,minute,second):
		current_time = datetime.strptime('{0}:{1}:{2}'.format(self.hour,self.minute,self.second), '%H:%M:%S')
		new_time = current_time + timedelta(days=0,hours=hour,minutes=minute,seconds=second)
		new_time_print = new_time.strftime('%H:%M:%S')
		print('new time: ',new_time_print)
		hour,minute,second = [int(j) for j in new_time_print.split(':')]
		self.set_time(hour,minute,second)










