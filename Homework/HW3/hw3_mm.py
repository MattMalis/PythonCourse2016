import tweepy
import time
import csv

auth = tweepy.OAuthHandler('jAzSxPFvOq2GIuXvNMNjJoB9e', 'GnOSfYMzQbrtfuY3lvxdJuqRFqBneRh6AghRIOea5EOVCvzoMf') 
auth.set_access_token('612416835-wEMoMN1R49XDZl8FuCNqI6Y3jdHPDChhqZOkJ9Ut', 'jmR7Udd0HhLPJE8wrrIBis1XzLKgZhZrKqqDY1Xgpnlab')    
api = tweepy.API(auth)

cfr = api.get_user('cfr_iigg')

# followers, followers_count, followers_ids,
# following, friends, friends_count, id, id_str, 
# screen_name, status, statuses_count
# cfr.status.created_at.day (.year, .month)

# 
# for item in items:
#     not_finished=True
#     while not_finished:
#         try:
# #            code
#             not_finished=False
#         except:
#             time.sleep(1)

## MOST ACTIVE = STATUSES_COUNT (total number of statuses)

cfr_fol_ids = []

while(True):
	try:
		cfr_fol_ids = cfr.followers_ids()
		break
	except:
		print "Error, sleeping and trying again"
		time.sleep(20)

## most active among followers of target

statuses = []
def get_fol_statuses(status_list, fol_id_list, start_index):
	#for index in range(start_index,10):
	for index in range(start_index,len(fol_id_list)):
		try:
			usr = api.get_user(fol_id_list[index])
			stat_count = usr.statuses_count
			status_list.append(stat_count)
		except:
			print "Error getting status count for follower id: %s (index #%s), sleeping and trying again" %(fol_id_list[index],index)
			time.sleep(20)
			get_fol_statuses(status_list, index)
	return status_list

cfr_fol_statuses = get_fol_statuses(statuses, cfr_fol_ids, 0)

## most popular (greatest # followers) among target's followers
fol_fol_list = []
fol_fol_count = []

## first - getting all followers' followers (will need it later)
# 	(to solve the current problem, just need to count)


def get_fol_fols(fol_fols, fol_fol_counts, fol_id_list, start_index):
	#for index in range(start_index,10):
	for index in range(start_index,len(fol_id_list)):
		try:
			
			usr = api.get_user(fol_id_list[index])
			count = usr.followers_count
			fol_fol_counts.append(count)
			fol_fols.append([])
			if count<=1000:
				for page in tweepy.Cursor(api.followers_ids, usr.screen_name).pages():
					fol_fols[index].extend(page)
			
		except:
			print "Error getting follower count for follower id: %s (index #%s), sleeping and trying again" %(cfr_fol_ids[index],index)
			time.sleep(20)
			get_fol_fols(fol_fols, fol_fol_counts, fol_id_list, index)
	return [fol_fols, fol_fol_counts]

cfr_combo = get_fol_fols(fol_fol_list, fol_fol_count, cfr_fol_ids, 0)
cfr_fol_fol_ids = cfr_combo[0]
cfr_fol_fol_counts = cfr_combo[0]

## getting friend IDs:

def: get_friend_ids():
	try:
		friend_ids = []
		friend_ids = cfr.friends_ids()
		return friend_ids
	except:
		print "error, trying again"
		time.sleep(20)
		get_friend_ids()
		
cfr_friend_ids = get_friend_ids()


## most active layman, expert, and celebrity among target's friends

fr_statuses = []
def get_fol_statuses(status_list, fr_id_list, start_index):
	#for index in range(start_index,10):
	for index in range(start_index,len(fr_id_list)):
		try:
			usr = api.get_user(fr_id_list[index])
			stat_count = usr.statuses_count
			status_list.append(stat_count)
		except:
			print "Error getting status count for follower id: %s (index #%s), sleeping and trying again" %(fol_id_list[index],index)
			time.sleep(20)
			get_fol_statuses(status_list, index)
	return status_list

cfr_fr_statuses = get_fol_statuses(fr_statuses, cfr_friend_ids, 0)


## most popular among friends of target

fr_fol_list = []
fr_fol_count = []

## first - getting all followers' followers (will need it later)
# 	(to solve the current problem, just need to count)

def get_fr_fols(fr_fols, fr_fol_counts, fr_id_list, start_index):
	for index in range(start_index,10):
	#for index in range(start_index,len(fr_id_list)):
		try:
			fr_fols.append([])
			usr = api.get_user(fr_id_list[index])
			count = usr.friend_count()
			fol_fol_counts.append(count)
			if count<=1000:
				2for page in tweepy.Cursor(api.followers_ids, usr.screen_name).pages():
					fol_fols[index].extend(page)
			#	ids = usr.followers_ids()
			#	fol_fols[index] = ids
		except:
			print "Error getting follower count for friend id: %s (index #%s), sleeping and trying again" %(cfr_fr_ids[index],index)
			time.sleep(20)
			get_fr_fols(fol_fols, fol_fol_counts, fol_id_list, index)
	return fol_fol_id_list

cfr_fr_fol_ids = get_fr_fols(fr_fol_list, fr_fol_count, cfr_fr_ids, 0)



## (limit the following to laymen (<100 followers) and experts (100-1000))

## most active among followers of target and their followers


## most active among followers of target and their friends




### writing to csv


c = open('cfr_twitter.csv','wb')
c_writer = csv.writer(c)
c_writer.writerow(["follower ID", "follower user name", "number of statuses" "number of followers"])

for i in range(len(:
	try:
		#c_writer.writerow([p[0], p[2], p[3], p[4]])
	except:
		print "ERROR: " + p[0] + '\n'
		pass

c.flush()
c.close()
