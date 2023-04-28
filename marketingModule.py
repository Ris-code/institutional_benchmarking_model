# Digital Marketing Metrics Calculator

# Get user input for website traffic
# website_traffic = int(input("Enter the total number of visitors to your website: "))

# # Get user input for traffic sources
# organic_search = int(input("Enter the number of visitors from organic search: "))
# direct_traffic = int(input("Enter the number of visitors from direct traffic: "))
# referral_traffic = int(input("Enter the number of visitors from referral traffic: "))
# social_media_traffic = int(input("Enter the number of visitors from social media: "))

# Calculate traffic by source percentages
def web_traffic_search(organic_search, direct_traffic, referral_traffic, social_media_traffic):
    
    total_traffic = organic_search + direct_traffic + referral_traffic + social_media_traffic
    organic_search_percentage = (organic_search / total_traffic) * 100
    direct_traffic_percentage = (direct_traffic / total_traffic) * 100
    referral_traffic_percentage = (referral_traffic / total_traffic) * 100
    social_media_traffic_percentage = (social_media_traffic / total_traffic) * 100

    return total_traffic, organic_search_percentage, direct_traffic_percentage, referral_traffic_percentage, social_media_traffic_percentage

# # Get user input for new vs. returning visitors and average session duration
# new_visitors = int(input("Enter the number of new visitors: "))
# returning_visitors = int(input("Enter the number of returning visitors: "))
# total_sessions = int(input("Enter the total number of sessions: "))
# average_session_duration = float(input("Enter the average session duration (in minutes): "))

# Calculate sessions per visitor and percentage of new vs. returning visitors
def new_vs_return_visitor(new_visitors, returning_visitors, total_sessions, average_session_duration):
    sessions_per_visitor = total_sessions / (new_visitors + returning_visitors)
    new_visitors_percentage = (new_visitors / (new_visitors + returning_visitors)) * 100
    returning_visitors_percentage = (returning_visitors / (new_visitors + returning_visitors)) * 100

    return sessions_per_visitor, new_visitors_percentage, returning_visitors_percentage

# Get user input for page views, most visited page, exit rate, and bounce rate
# page_views = int(input("Enter the total number of page views: "))
# most_visited_page = input("Enter the URL of the most visited page: ")
# exit_rate = float(input("Enter the exit rate (%): "))
# bounce_rate = float(input("Enter the bounce rate (%): "))

# Calculate total exits and total bounces
def exit_and_total_bounces(page_views, exit_rate, bounce_rate):
    total_exits = int(page_views * (exit_rate / 100))
    total_bounces = int(page_views * (bounce_rate / 100))

    return total_exits, total_bounces

# # Get user input for conversions and cost per click
# conversions = int(input("Enter the total number of conversions: "))
# cost_per_click = float(input("Enter the cost per click: "))

# Calculate conversion rate, cost per conversion, and cost per acquisition
def conversion_rate(conversions, cost_per_click, total_traffic):
    conversion_rate = (conversions / total_traffic) * 100
    cost_per_conversion = cost_per_click * (total_traffic / conversions)
    cost_per_acquisition = cost_per_click * (total_traffic / conversions) * (1 / conversion_rate)
    
    return conversion_rate, cost_per_conversion, cost_per_acquisition

# # Get user input for email metrics
# email_opens = int(input("Enter the total number of email opens: "))
# email_clicks = int(input("Enter the total number of email clicks: "))
# emails_sent = int(input("Enter the total number of emails sent: "))

# Calculate email open rate and email click-through rate
def email_open_rate(email_opens, email_clicks, emails_sent):
    email_open_rate = (email_opens / emails_sent) * 100
    email_click_through_rate = (email_clicks / email_opens) * 100

    return email_open_rate, email_click_through_rate

# # Get user input for social media metrics
# impressions = int(input("Enter the total number of impressions: "))
# # social_reach = int(input("Enter the total social media reach: "))
# social_engagement = int(input("Enter the total social media engagement: "))

#Calculate engagement rate, cost per impression, and overall ROI
def engagement_rate(impressions, social_engagement):
    engagement_rate = (social_engagement / impressions) * 100

    return engagement_rate
    # cost_per_impression = total_cost / impressions
# overall_roi = ((total_revenue - total_cost) / total_cost) * 100

#Print out all the calculated metrics
# print("Traffic by Source:")
# print(f"Organic Search: {organic_search_percentage:.2f}%")
# print(f"Direct Traffic: {direct_traffic_percentage:.2f}%")
# print(f"Referral Traffic: {referral_traffic_percentage:.2f}%")
# print(f"Social Media Traffic: {social_media_traffic_percentage:.2f}%\n")

# print("New vs. Returning Visitors:")
# print(f"New Visitors: {new_visitors_percentage:.2f}%")
# print(f"Returning Visitors: {returning_visitors_percentage:.2f}%")
# print(f"Sessions per Visitor: {sessions_per_visitor:.2f}")
# print(f"Average Session Duration: {average_session_duration:.2f} minutes\n")

# print("Page Views:")
# print(f"Total Page Views: {page_views}")
# print(f"Most Visited Page: {most_visited_page}")
# print(f"Exit Rate: {exit_rate}%")
# print(f"Total Exits: {total_exits}")
# print(f"Bounce Rate: {bounce_rate}%")
# print(f"Total Bounces: {total_bounces}\n")

# print("Conversion Metrics:")
# print(f"Conversion Rate: {conversion_rate:.2f}%")
# print(f"Cost per Click: ${cost_per_click:.2f}")
# print(f"Cost per Conversion: ${cost_per_conversion:.2f}")
# print(f"Cost per Acquisition: ${cost_per_acquisition:.2f}\n")

# print("Email Metrics:")
# print(f"Email Open Rate: {email_open_rate:.2f}%")
# print(f"Email Click-Through Rate: {email_click_through_rate:.2f}%\n")

# print("Social Media Metrics:")
# print(f"Impressions: {impressions}")
# print(f"Social Reach: {social_reach}")
# print(f"Social Engagement: {social_engagement}")
# print(f"Engagement Rate: {engagement_rate:.2f}%")
# print(f"Cost per Impression: ${cost_per_impression:.2f}\n")

# print("ROI Metrics:")
# print(f"Total Revenue: ${total_revenue:.2f}")
# print(f"Total Cost: ${total_cost:.2f}")
# print(f"Overall ROI: {overall_roi:.2f}%")