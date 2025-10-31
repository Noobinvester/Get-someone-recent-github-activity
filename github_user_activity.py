from github import Github

username = input("Enter GitHub username: ")
print("Starting GitHub user activity fetcher...")

g = Github()
try:
    user = g.get_user(username)

    
    repos = user.get_repos(sort="created", direction="desc")
    print(f"\nRecent repositories created by {username}:")
    print("--------------------------------------------------")
    for i, repo in enumerate(list(repos)[:5], start=1):
        print(f"{i}. {repo.name} - Created: {repo.created_at}")
    
   
    starred = user.get_starred()  
    print(f"\nRecent repositories starred by {username}:")
    print("--------------------------------------------------")
    for i, repo in enumerate(list(starred)[:5], start=1):
        print(f"{i}. {repo.full_name} - ⭐ {repo.stargazers_count} stars")
    
    # Recent issue activity
    events = user.get_events() 
    issue_found = False
    
    print(f"\nRecent issue activity by {username}:")
    print("--------------------------------------------------")
    
    for event in events:  
        if event.type == "IssuesEvent":  
            if event.payload['action'] == "opened":
                issue = event.payload['issue']
                print(f"🆕 Opened Issue: {issue['title']}")
                print(f"   Repo: {event.repo.name}")
                print(f"   Date: {event.created_at}\n")
                issue_found = True
    
    if not issue_found:
        print(f"No recent issues opened by {username}.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("\nMake sure the username is correct and you have an active internet connection.")

finally:
    g.close()