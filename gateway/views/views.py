from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

def community_view(request):
	myVenture = {
		"title": "My Ventures",
		"content": "Start a new venture today!"
	}
	groupVenture = {
		"title": "My Groups's Ventures",
		"content": "You do not yet have any groups. Start a venture to become part of a group."
	}
	communityVenture = {
		"title": "Community Ventures",
		"content": "John Smith just published his first survey! Gateway helped Planet Express start their own business. Read the story and see how their company is doing now. You too, could be running your own business someday!"
	}
    	return render(request, 'community.html', dict(myVenture=myVenture, groupVenture=groupVenture, communityVenture=communityVenture) )

def home_view(request):
    return render(request, 'home.html')

def members_view(request):
	news = [
		{
			"title": "Happy New Year!",
			"date": "1.1.2014"
		},
		{
			"title": "Planet Express has made their first delivery!",
			"date": "21.12.2013"
		},
		{
			"title": "Today in 1982 Bill Gates made his first dollar!",
			"date": "14.12.2013"
		}
	]
	currentVenture = {
		"image": "glyphicon-briefcase",
		"title": "Current Venture",
		"description": "You're doing good! Keep it up!"
	}
    	return render(request, 'members.html', dict(news=news, currentVenture=currentVenture) )

def minigames_view(request):
	minigame = {
		"title": "Minigames",
		"subtitle": "Coming Soon!"
	}
    	return render(request, 'minigames.html', dict(minigame=minigame) )

def profile_view(request):
	user = {
		"name": "John Smith",
		"email": "John.Smith@email.com"
	}
    	return render(request, 'profile.html', dict(user=user))

def ventures_view(request):
	ventures = [
		{
			"image": "glyphicon-book",
			"title": "Book Store",
			"description": "Your chain of bookstores Borders isn't doing so well."
		},
		{
			"image": "glyphicon-phone-alt",
			"title": "Call Center",
			"description": "Your help office has collapsed, killing all the workers. But you have collected 200% with insurance fraud! You're a real tycoon!"
		},
		{
			"image": "glyphicon-music",
			"title": "Music Business",
			"description": "Your website Napster has been shutdown by U.S. authorities. Better luck next time."
		}
	]
	currentVenture = {
		"image": "glyphicon-briefcase",
		"title": "Current Venture",
		"description": "You're doing good! Keep it up!"
	}
    	return render(request, 'ventures.html', dict(ventures=ventures, currentVenture=currentVenture) )