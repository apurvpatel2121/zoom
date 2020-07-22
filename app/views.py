import json
from zoomus import ZoomClient

from django.shortcuts import render
client = ZoomClient('p2vfoI2rRHeKadOyf5ZVvw', 'o2nWnDLhyBFBmSSx6xs9uaFB4tVOSP0t6j0w')

# Create your views here.
def all(request):
    
    return render(request,'main.html')


def create(request):
    meet = client.meeting.create(
    user_id='apurvpatel2121@gmail.com',
	)
    user = json.loads(meet.content)
    join = user['start_url']
    context = {
		"json":join
	}
    return render(request,'index.html',context)



def list(request):
    meet = client.meeting.list(
    user_id='apurvpatel2121@gmail.com',
	)
    user = json.loads(meet.content)
    join = user['meetings'][-1]['join_url']
    context = {
		"json":join
	}
    return render(request,'list.html',context)