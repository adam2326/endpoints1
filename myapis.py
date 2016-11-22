
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote



# create the different types of responses to send
class text_response_only(messages.Message):
	"""String that stores a message."""
	resp = messages.StringField(1)


# create an overall statistical text API class
@endpoints.api(name='statistical_tests', version='v1')
class statistical_tests(remote.Service):
	"""statistical test API v1"""


	# define a specific statistical test - t-test for two sample means
	@enpoints.method(message_types.VoidMessage , name='ttest_for_two_sample_means', path='ttest', method='GET'):
	def (self, request):
		"""docs go here"""
		return text_response_only(resp="hello ttester")

app = endpoints.api_server([statistical_tests])