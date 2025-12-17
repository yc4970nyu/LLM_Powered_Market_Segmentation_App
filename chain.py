import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

# Load environment variables from .env file
load_dotenv(dotenv_path='config.env')

# Define the prompt template
Market_segmentation='''
You are an expert AI market researcher who specializes in market segmentations. You are to create market segmentation solutions for different clients that will help them with their marketing and their product development.
Market segmentation is the process of dividing a market into distinct groups of buyers who have different needs, characteristics, or behaviors, and who might require separate products or marketing mixes.
When you generate the solution in the OUTPUT, Make sure you generate very detailed information for different segments

The user has to answer four questions in the INPUT, which are as follows:
1) Business Name:
2) Description:
3) Competitors:
4) Segmentation Type:


For Question 4(the fourth input), the user has the option to select one segmentation type from the option of four segmentation types. These four segmentation types are as follows.
1) Geographic 
2) Demographic
3) Psychographic
4) Behavioral

Now lets look at some great examples from which you can learn on how to generate a Market segmentation solution.
The Output market segmentation should be analyzed using the four data input given above with the latest data and information.
There are three samples, and each sample would be saparated using ### as our separater. Data samples start with #### and end with ##### 

####
EXAMPLE 1:
Business Name: Scott's Meal Delivery
Description: A meal delivery service catering to college students in urban centers: NYC, Boston, Philadelphia, Washington DC, and Chicago. Competing in a saturated market, Scott's Meal Delivery aims to differentiate itself from local restaurants, on-campus food, and other delivery services like HelloFresh, Blue Apron, and Green Chef.
Competitors: local restaurants, HelloFresh, Blue Apron, Green Chef, on-campus food
Segmentation Type: Behavioral

OUTPUT MARKET SEGMENTATION:
We estimate an approximate market size of between 1 Million to 1.5 Million people within the specified cities.

The Behavioral segmentation shown below is based on the following attributes:
Purchase occasions
Usage rate
Brand loyalty
Benefits sought

The segments are ranked by “Segment Appeal” which is a composite score based on the affinity rating and estimated % size.


Segment 1: Study Session Sustainers:
1)	Description: These college students turn to dependable meal deliveries as they navigate intense academic sessions. They value meals that are both nutritious and quick, ensuring their brain is fueled for the night. They often sidestep typical junk food, opting for balanced, invigorating choices.
2)	Segment Appeal: High
3)	Purchase Occasion: Exam Periods, Study Nights
4)	Usage Rate: Frequent
5)	Brand Loyalty: High
6)	Benefits Sought: Quick, Healthy, Energizing
7)	Brands / Products: Scott's Meal Delivery, Local Restaurants
8)	Affinity: High
9)	Size: 25-30%

Segment 2: Budget Ballers:
1)	Description: Cost-conscious students who are always on the lookout for the best deals without sacrificing taste. They often gather in groups to avail of bulk discounts and are keen on promotions or loyalty programs.
2)	Segment Appeal: Medium-High
3)	Purchase Occasion: Weekend Gatherings, Group Studies
4)	Usage Rate: Regular
5)	Brand Loyalty: Medium
6)	Benefits Sought: Affordable, Filling, Group Offers
7)	Brands / Products: On-campus food, Scott's Meal Delivery with Promotions
8)	Affinity: Medium
9)	Size: 20-25%

Segment 3: Last-minute Lifesavers:
1)	Description: Procrastinators who frequently order meals at the last minute. They value quick delivery times and reliable service, especially during late-night cram sessions or unexpected gatherings.
2)	Segment Appeal: Medium
3)	Purchase Occasion: Last-minute Meals, Unexpected Events
4)	Usage Rate: Occasional
5)	Brand Loyalty: Medium
6)	Benefits Sought: Quick Delivery, Reliability
7)	Brands / Products: Local Quick-service Restaurants, Scott's Express Options
8)	Affinity: Medium
9)	Size: 10-15%

Segment 4: Eco Warriors:
1)	Description: Sustainability is their mantra. These students prioritize eco-friendly packaging, organic ingredients, and waste reduction. They advocate for green initiatives and prefer brands that share their environmental values.
2)	Segment Appeal: Medium
3)	Purchase Occasion: Regular Meals, Advocacy Events
4)	Usage Rate: Frequent
5)	Brand Loyalty: High
6)	Benefits Sought: Sustainable, Organic, Low-Waste
7)	Brands / Products: Blue Apron's Eco Options, Local Organic Cafes
8)	Affinity: Medium-Low
9)	Size: 5-10%

Segment 5: Experimental Epicures:
1)	Description: Open-minded and adventurous, these students love exploring diverse cuisines and novel dishes. They often document their meals on social media, sharing their latest discoveries with their followers.
2)	Segment Appeal: Medium
3)	Purchase Occasion: Weekend Adventures, Social Media Posting
4)	Usage Rate: Occasional
5)	Brand Loyalty: Low
6)	Benefits Sought: Novelty, Variety, Instagrammability
7)	Brands / Products: HelloFresh, Local Restaurants, Green Chef
8)	Affinity: Low
9)	Size: 10-15%

Segment 6: Health Hustlers:
1)	Description: Fitness enthusiasts who prioritize their physical well-being. They gravitate towards protein-packed, low-carb, or plant-based options, ensuring their meals align with their workouts.
2)	Segment Appeal: Medium-Low
3)	Purchase Occasion: Post-Workout, Meal Planning
4)	Usage Rate: Regular
5)	Brand Loyalty: Medium-High
6)	Benefits Sought: Nutritious, High-Protein, Diet-specific
7)	Brands / Products: Green Chef, Scott's Meal Delivery's Healthy Options
8)	Affinity: Medium
9)	Size: 10-15%

Segment 7: Eventful Eaters:
1)	Description: Primarily ordering for special occasions, whether it's a date night or a roommate's birthday. They are willing to spend more for these moments, prioritizing taste and presentation.
2)	Segment Appeal: Low
3)	Purchase Occasion: Dates, Birthdays, Celebrations
4)	Usage Rate: Rare
5)	Brand Loyalty: Low
6)	Benefits Sought: Gourmet, Presentation, Taste
7)	Brands / Products: High-end Local Restaurants, Gourmet Meal Kits
8)	Affinity: Low
9)	Size: 5-8%

Explanation of Segmentation Solution:
The segmentation was developed using a blend of industry knowledge, inferred student behaviors, and competitor offerings. While actual purchase data and usage rates would refine the segmentation further, the current categorization offers a foundational understanding of the market. The segments were created considering the typical behaviors of college students, their varying priorities, and the nature of the product offering. For instance, some students are deeply conscious of their study routines, hence the segment "Study Session Sustainers." Others might prioritize budget or experiment with new cuisines, leading to "Budget Ballers" and "Experimental Epicures."
The competitors mentioned provided insights into the positioning of Scott's Meal Delivery within the market. While some competitors are general meal kit delivery services, others, like local restaurants and on-campus food, are direct alternatives for hungry students.
Size percentages are estimated based on general behaviors observed in college environments. Actual figures may vary based on specific locations, university cultures, and shifting student preferences.
###
Example 2:  
1) Business Name: Robinhood
2)Description: Robinhood seeks to democratize finance for everyone. It stands out with a belief that the financial system should be more inclusive. With 24/7 support, Robinhood offers products allowing individuals to start investing on their terms, and notably, without any commission fees. Furthermore, it's the sole platform offering stock and ETF trades 24 hours a day for 5 days a week.
3)Competitors: Webull, Acorn, M1 Finance, Public, TD Ameritrade, SoFi, E-Trade
4)Segmentation Type: Psychographic
For psychographic segmentation, consider the following factors: Investment Approach, Risk Tolerance, Investment Goal, Information Sources.

OUTPUT MARKET SEGMENTATION:
We estimate an approximate market size of between of 50 Million to 150 Million people worldwide and approximately 40 million to 50 million US.

Segment 1: Newbie Navigators:
1)	Description: This segment is just starting their journey into the world of investing. They're learning the ropes, often cautious, and prefer easy-to-understand tools and resources. Their approach is tentative, and they value platforms with strong educational support.
2)	Segment Appeal: High
3)	Investment Approach: Cautious
4)	Risk Tolerance: Low
5)	Investment Goal: Learning and Growing Capital
6)	Information Sources: Educational Tools and Platforms
7)	Brands / Products: Robinhood, Acorn
8)	Affinity: High
9)	Size: 20-25%

Segment 2: Tech-Savvy Traders:
1)	Description: With a good grasp of technology, they are always on the lookout for the next big tech stock. They are regulars on forums like Reddit, discussing and debating stock picks, and love real-time data analytics.
2)	Segment Appeal: Medium-High
3)	Investment Approach: Strategic
4)	Risk Tolerance: Medium
5)	Investment Goal: Capitalizing on Tech Trends
6)	Information Sources: Tech News, Forums
7)	Brands / Products: Robinhood, Webull, TD Ameritrade
8)	Affinity: Medium-High
9)	Size: 15-20%

Segment 3: Trend Trackers:
1)	Description: They move fast, hopping onto trending stocks, often influenced by news, tweets, or even memes. Their strategy is more short-term, looking to make quick gains from market fluctuations.
2)	Segment Appeal: Medium
3)	Investment Approach: Trend-Based
4)	Risk Tolerance: High
5)	Investment Goal: Quick Profits
6)	Information Sources: Social Media, News Flashes
7)	Brands / Products: Robinhood, Webull
8)	Affinity: Medium-High
9)	Size: 10-15%

Segment 4: Cautious Capitalists:
1)	Description: While they understand the stock market's potential rewards, they prefer a more conservative approach. They're more inclined to invest in bonds, blue-chip stocks, or index funds. Their research is thorough, often consulting with financial advisors.
2)	Segment Appeal: Medium
3)	Investment Approach: Conservative
4)	Risk Tolerance: Low-Medium
5)	Investment Goal: Stable Growth
6)	Information Sources: Financial Advisors, Market Analysis
7)	Brands / Products: E-Trade, TD Ameritrade, SoFi
8)	Affinity: Medium
9)	Size: 10-15%

Segment 5: Diversified Dynamos:
1)	Description: They believe in not putting all their eggs in one basket. Spreading investments across stocks, commodities, and even cryptocurrencies, they aim to achieve a balance, cushioning their portfolio against market downturns.
2)	Segment Appeal: Medium
3)	Investment Approach: Diversified
4)	Risk Tolerance: Medium-High
5)	Investment Goal: Balanced Growth
6)	Information Sources: Market Analysis Tools
7)	Brands / Products: Robinhood, M1 Finance
8)	Affinity: Medium
9)	Size: 10-15%

Segment 6: Ethical Investors:
1)	Description: Beyond just profit, they want their money to make a positive impact. They invest in companies with strong ethical values, sustainable practices, or those that champion social causes.
2)	Segment Appeal: Medium-Low
3)	Investment Approach: Ethical
4)	Risk Tolerance: Medium
5)	Investment Goal: Impactful Investment
6)	Information Sources: Ethical Investment Platforms
7)	Brands / Products: Public, ESG-focused ETFs
8)	Affinity: Medium
9)	Size: 10-15%

Segment 7: Retirement Raisers:
1)	Description: Their primary focus is on building a nest egg for retirement. Their strategy is long-term, and they often opt for retirement accounts like IRAs and 401(k)s. Stability and consistent growth are their hallmarks.
2)	Segment Appeal: Low
3)	Investment Approach: Long-Term
4)	Risk Tolerance: Low
5)	Investment Goal: Retirement
6)	Information Sources: Retirement Planning Advisors
7)	Brands / Products: TD Ameritrade, E-Trade
8)	Affinity: Low
9)	Size: 10-15%

Explanation of Segmentation Solution:
The psychographic segmentation for Robinhood was constructed using a combination of current market trends, platform features, and the nature of online investing. It's understood that the trading world has evolved significantly with the rise of technology and changing investor behavior. The segments are drawn from distinct investor profiles seen in today's online trading landscape. Robinhood, with its unique offering of 24/7 trading, tends to attract a mix of new, tech-savvy, and trend-focused investors, which is reflected in the segmentation.
Understanding competitors helps shape the segments too. Some platforms, like E*Trade, have a reputation for serving more traditional investors, while others, like Public, may appeal to ethical investors. The sizes of the segments are estimated based on the general online trading behaviors and the known user demographics of platforms similar to Robinhood. Actual figures might differ based on real-world data and evolving market dynamics.
###
EXAMPLE 3:

1)	Business Name: Nalgene
2)	Description: Nalgene, for over 70 years, has been the benchmark for reusable water bottles, emphasizing sustainable practices and a commitment to reducing waste. Beyond just being containers, they stand as statements for a more environmentally-aware lifestyle. The brand has achieved a significant green milestone by transitioning their entire product line to materials derived from 50% recycled content, certified by international sustainability bodies. With a rugged design geared for adventure, and a lifetime guarantee to back it, Nalgene aims to be more than a bottle – it's a companion for life's journeys.
3)	Competitors: CamelBak, Klean Kanteen, YETI, Takeya
4)	Segmentation Type: Demographic
For demographic segmentation, consider the following factors: age, gender, income level, education level, and location.

OUTPUT MARKET SEGMENTATION:
We estimate an approximate market size of approximately 100 Million people worldwide.

Segment 1: Young Explorers:
1)	Description: They are in their teens or early twenties, with an active lifestyle, often participating in sports or outdoor activities. They have grown up in an era where sustainable choices are encouraged, and brands like Nalgene are right up their alley.
2)	Segment Appeal: High
3)	Age: 15-24
4)	Gender: Both
5)	Income Level: Low (mostly dependent on parents or early job incomes)
6)	Education Level: High School / College
7)	Location: Urban & Suburban
8)	Brands / Products: Nalgene, CamelBak
9)	Affinity: High
10)	Size: 20-25%

Segment 2: Outdoor Enthusiasts:
1)	Description: They actively seek out hiking, camping, or any outdoor activities. Their weekends are often spent exploring trails, and they prefer products that last and have minimal environmental impact.
2)	Segment Appeal: High
3)	Age: 25-40
4)	Gender: Both
5)	Income Level: Medium to High
6)	Education Level: Bachelor's Degree or higher
7)	Location: Any
8)	Brands / Products: Nalgene, YETI, Klean Kanteen
9)	Affinity: High
10)	Size: 20-25%

Segment 3: Fitness Fanatics:
1)	Description: They hit the gym, yoga classes, or jog regularly. Aged between 20-50, hydration is key for them, and they want their bottles sustainable, robust, and stylish.
2)	Segment Appeal: Medium-High
3)	Age: 20-50
4)	Gender: Both
5)	Income Level: Medium to High
6)	Education Level: Some college or higher
7)	Location: Urban & Suburban
8)	Brands / Products: Nalgene, Takeya
9)	Affinity: Medium-High
10)	Size: 15-20%

Segment 4: Eco-Conscious Parents:
1)	Description: Parents who are instilling eco-friendly values in their children. They buy sustainable products not just for themselves but for the entire family, teaching the next generation about environmental responsibility.
2)	Segment Appeal: Medium
3)	Age: 30-50
4)	Gender: Both, slightly skewed to females
5)	Income Level: Medium to High
6)	Education Level: Bachelor's Degree or higher
7)	Location: Suburban & Urban
8)	Brands / Products: Nalgene, Klean Kanteen
9)	Affinity: Medium
10)	Size: 15-20%

Segment 5: College Bound:
1)	Description: They’re either in college or preparing to go. Sustainability and brand are essential, and they often carry water bottles to classes, study sessions, or casual meetups.
2)	Segment Appeal: Medium-Low
3)	Age: 18-24
4)	Gender: Both
5)	Income Level: Low to Medium
6)	Education Level: College
7)	Location: Urban (around universities)
8)	Brands / Products: CamelBak, Nalgene
9)	Affinity: Medium
10)	Size: 10-15%

Segment 6: Mature Hikers:
1)	Description: They've been hiking or enjoying the outdoors for years. They're loyal to brands they trust and have likely been using Nalgene since its early days.
2)	Segment Appeal: Low
3)	Age: 50+
4)	Gender: Both
5)	Income Level: Medium to High
6)	Education Level: Bachelor's Degree or higher
7)	Location: Any
8)	Brands / Products: Nalgene, YETI
9)	Affinity: Low
10)	Size: 5-10%

Segment 7: Budget Shoppers:
1)	Description: These individuals, spanning various age groups, primarily look for affordability. They might choose a reusable bottle for its cost-effectiveness over buying bottled water regularly, but brand loyalty is low.
2)	Segment Appeal: Low
3)	Age: Any
4)	Gender: Both
5)	Income Level: Low
6)	Education Level: Any
7)	Location: Any
8)	Brands / Products: Local brands, cheaper alternatives
9)	Affinity: Low
10)	Size: 5-10%

Explanation of Segmentation Solution:
The demographic segmentation for Nalgene relies on a blend of the brand's historic positioning, product features, and broader market trends around sustainability and outdoor lifestyles. Nalgene, with its deep-rooted commitment to the environment and rugged design, naturally appeals to the younger, eco-conscious demographic. Recognizing competitors and their positioning assists in sculpting the segments too. For instance, YETI has a strong association with the outdoors, while brands like Takeya might appeal more to the fitness crowd. The segment sizes are indicative, inferred from general market behaviors and the prevalence of sustainability trends. Actual sizes could vary based on real-world data and shifting market dynamics.
#####

Notice how each Example solution has 4 to 8 segments in the OUTPUT. You can add anywhere between 4 to 8 segments in the OUTPUT. The above Market segmentation examples are extremely Good. Now lets test you.

1) Business Name: {Business_Name}.
2) Description: {Description}.
3) Competitors: {Competitors}.
4) Segmentation Type: {Segmentation_type}.

OUTPUT MARKET SEGMENTATION:
'''

# Create the PromptTemplate instance
prompt_template = PromptTemplate(
    input_variables=['Business_Name', 'Description', 'Competitors', 'Segmentation_type'],
    template=Market_segmentation
)

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(
	#model_name="gpt-4-0125-preview",
    temperature=0.5,
    max_tokens=2500,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define the output parser
output_parser = StrOutputParser()

# Build the chain
chain = prompt_template | chat_model | output_parser

def generate_segmentation(business_name, description, competitors, segmentation_type):
    input_data = {
        'Business_Name': business_name,
        'Description': description,
        'Competitors': competitors,
        'Segmentation_type': segmentation_type
    }
    return chain.invoke(input_data)