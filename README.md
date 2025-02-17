# Apple Store Review Analysis API

This project provides an API for collecting, processing, and analyzing Apple Store reviews. It collects 100 random reviews for a specified app, processes the data to extract key fields, calculates metrics, performs sentiment analysis, groups negative reviews using BERTopic, and extracts keywords from negative reviews using TF-IDF. The API also supports visualization endpoints that return images (as base64-encoded PNGs) for charts generated with Altair.

## File Structure

.
├── main.py
├── pyproject.toml
├── README.md
└── src
└── nebula_demo
├── init.py
├── data_collection.py
├── data_processing.py
├── metrics.py
├── insights.py
└── vis.py

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/apple_store_review_analysis.git
   cd apple_store_review_analysis

	2.	Install Dependencies
This project uses Poetry for dependency management. Install Poetry if you haven’t already, then run:

poetry install

Alternatively, you can install dependencies manually using pip:

pip install fastapi uvicorn uvloop requests polars nltk bertopic scikit-learn altair loguru

Note: To generate images from Altair charts, you may need to install additional dependencies (e.g., altair_saver) and ensure that a supported image export method (such as Selenium or VLC) is available.

	3.	Run the API Locally
Start the API with Uvicorn (which uses uvloop for improved performance):

poetry run python main.py

The API will be available at: http://127.0.0.1:8000

API Endpoints
	•	GET /collect?app_id=YOUR_APP_ID
Collects raw review data for the specified app.
	•	GET /metrics?app_id=YOUR_APP_ID
Processes reviews, calculates metrics (average rating, rating distribution, etc.), performs sentiment analysis, and generates insights.
	•	GET /download?app_id=YOUR_APP_ID
Downloads the raw review data as a JSON file.
	•	GET /visualize?app_id=YOUR_APP_ID
Generates and returns visualization images for:
	•	Rating Distribution (bar chart)
	•	Sentiment Distribution (arc chart)
The images are returned as base64-encoded PNG strings that can be rendered in any compatible viewer.

Visualization

The file src/nebula_demo/vis.py contains functions to create Altair charts:
	•	Rating Distribution: A bar chart showing the count of reviews per rating.
	•	Sentiment Distribution: An arc (pie-like) chart showing the percentage of positive, neutral, and negative reviews.

The /visualize endpoint converts these charts to images and returns them as base64-encoded PNGs.

Logging

The API extensively uses loguru for logging. Logs will appear in the console to help trace operations and diagnose issues.

Sample Report

A sample report for a chosen app may include:
	•	Metrics:
	•	Average Rating, Median Rating, Total Reviews
	•	Rating Distribution (e.g., percentage of 5-star, 4-star reviews)
	•	Insights:
	•	Sentiment counts (e.g., 60 positive, 25 neutral, 15 negative)
	•	Grouped topics from negative reviews (using BERTopic)
	•	Top keywords in negative reviews (e.g., “bug”, “crash”, “slow”)

Use the /metrics endpoint to generate these insights and /visualize to obtain the charts for further analysis.

Happy analyzing!

# Results

## Collect

Request:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/collect?app_id=1459969523' \
  -H 'accept: application/json'
```

Output:
```json
{
  "feed": {
    "entry": [
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id42931861"
          },
          "name": {
            "label": "Gemini-21"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-03-02T17:41:46-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.4.0"
        },
        "id": {
          "label": "7058559617"
        },
        "title": {
          "label": "Entertaining"
        },
        "content": {
          "label": "Fantastic and quit entertaining, great quality and everything works. However too expensive for me. Maybe one day I’ll buy it if I win the notational lottery!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id677314918"
          },
          "name": {
            "label": "DB🥳"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-04-06T01:17:50-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "2.0"
        },
        "id": {
          "label": "5769985985"
        },
        "title": {
          "label": "Great app!"
        },
        "content": {
          "label": "Really accurate & functions really well.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id888014166"
          },
          "name": {
            "label": "I COULD' VE DROPPED MY 🥐"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-05-19T06:17:07-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "2.3.1"
        },
        "id": {
          "label": "5965681303"
        },
        "title": {
          "label": "Good! But..."
        },
        "content": {
          "label": "I'm a 12 year old who loves astrology. I really like the features in this app but i do have a slight problem. i'm not allowed to pay money on my phone. I really wish i could check my compatibility without having to watch a video before. overall, this is a good app. btw im sun in aquarius, moon in scorpio and aries rising 😉",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "1"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "1"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1119607791"
          },
          "name": {
            "label": ",c,dsl"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-05-24T12:23:50-07:00"
        },
        "im:rating": {
          "label": "3"
        },
        "im:version": {
          "label": "4.8.0"
        },
        "id": {
          "label": "7383621522"
        },
        "title": {
          "label": "Eh"
        },
        "content": {
          "label": "For me this app would be real good but every 2 seconds it’s like press her and then it’s like PAY TO USE THIS so not the best app but my to bad 👍🏾",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id662612012"
          },
          "name": {
            "label": "sgear72"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-06-04T11:22:15-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.23.0"
        },
        "id": {
          "label": "11343330677"
        },
        "title": {
          "label": "Taken my money without my consent"
        },
        "content": {
          "label": "Taken money out of my account without having an active account with them avoid !!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id12300004"
          },
          "name": {
            "label": "Lauralilyamy"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-08-03T01:58:42-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.34.0"
        },
        "id": {
          "label": "8940100446"
        },
        "title": {
          "label": "Charged £35.81 despite cancelling"
        },
        "content": {
          "label": "I have cancelled my subscription but have been charged twice in the last week a total of £35.81.\n\nCustomer service do not reply, this is literally theft.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1259815965"
          },
          "name": {
            "label": "Leto-Huntress"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-10-04T20:28:56-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.39.0"
        },
        "id": {
          "label": "11798565938"
        },
        "title": {
          "label": "Be careful!!!"
        },
        "content": {
          "label": "They will take £33 a month after the trial period even if you deactivate your account. Thankfully my were straight on it and I managed to get a refund. Make sure you cancel your subscription whether that’s through Apple or Google store or your bank to check if they’ve set up a recurring payment.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id324534648"
          },
          "name": {
            "label": "Tess4032"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-24T16:36:03-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.61.0"
        },
        "id": {
          "label": "12226904874"
        },
        "title": {
          "label": "Scam"
        },
        "content": {
          "label": "You took money without my authorisation please pay it back",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1631832647"
          },
          "name": {
            "label": "I don’t usually rate"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-03-04T14:22:38-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.04.0"
        },
        "id": {
          "label": "11008695349"
        },
        "title": {
          "label": "Request payment without asking permission"
        },
        "content": {
          "label": "You will receive the multiple requests of one payment usually, but this app doesn’t have. It just takes your money directly without second make-sure enquiry.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id615669306"
          },
          "name": {
            "label": "Cyc 101"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-09-22T01:59:40-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.37.0"
        },
        "id": {
          "label": "11751450188"
        },
        "title": {
          "label": "This app just wanna take your money"
        },
        "content": {
          "label": "I have paid €1 for the reading and skipped all the offers, however it has charged me for another $49.99… for the offer that I didn’t click to purchase. As I have experiences in dealing with these sales pages, I take extra attention to those small words etc cause this is how company TRICK YOU TO BUY MORE THINGS THAT YOU ARE NOT AWARE OF! So I clicked the skipped the offer but still being charged… Just really not a fan for this kind of app… esp in a spiritual industry that you should help people but not take away people’s money … (Hope I won’t get a “sorry for your dissatisfaction” comment, but actually have someone from the company fully refund me cause I already contacted to one of your team member and said offer me 50% refund. I definitely not gonna accept for something that I didn’t purchase 😂) Mistakes need actions to improve. Found all reviews said this app is a spam is really helpful…",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1231928600"
          },
          "name": {
            "label": "I send harsh comments"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-03-11T22:28:10-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "4.23.0"
        },
        "id": {
          "label": "8446276372"
        },
        "title": {
          "label": "A request"
        },
        "content": {
          "label": "In this app, it has star signs, yes? There aren’t  any opportunities to do a cusp sign. If you could add an option to cusp signs that would help. Thank you.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id15530006"
          },
          "name": {
            "label": "shelly_c"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-08-09T01:13:42-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.32.0"
        },
        "id": {
          "label": "11589320082"
        },
        "title": {
          "label": "Scam"
        },
        "content": {
          "label": "I got absolutely bombarded with ads and when I started a free 3-day trial I clicked on a link that said I could get a reading for €1, I paid this, clicked on “get my reading” and was immediately charged €29.99 (unknown to myself) of which I had no confirmation, just a blank page, upon reloading I was charged again and got a confirmation from my bank about 2 identical charges. DON’T CLICK ON ANYTHING!!!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1021432557"
          },
          "name": {
            "label": "oxf.charrrr"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-08-12T03:45:06-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.32.0"
        },
        "id": {
          "label": "11600748657"
        },
        "title": {
          "label": "Can not use without paying"
        },
        "content": {
          "label": "I use to love nebula but ever since the new premium update to get any reading about your birth chart or housing you have to pay for premium, all features are basically premium such a disappointment it use to be the best star sign app :(",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id311031231"
          },
          "name": {
            "label": "donascy"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-13T00:48:53-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.55.0"
        },
        "id": {
          "label": "12057684295"
        },
        "title": {
          "label": "Nebula is great!"
        },
        "content": {
          "label": "I have the app for about 5 years and really enjoy reading my daily horoscope and talk to some astrologers and psychics on regular basis.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id979801586"
          },
          "name": {
            "label": "memaidqueenine"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-10-02T07:18:13-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.13.0"
        },
        "id": {
          "label": "7869460916"
        },
        "title": {
          "label": "LOVE IT"
        },
        "content": {
          "label": "This app is amazing it’s like my friend she new what my zodiac sign was and it was cancer ♋️ but apparently NASA has realised the zodiacs and my zodiac has been shifted .If anyone’s zodiac has been shifted nebula is the win",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id130983526"
          },
          "name": {
            "label": "xxTYZxx"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-12T06:31:28-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "5.64.0"
        },
        "id": {
          "label": "12302296590"
        },
        "title": {
          "label": "Very good app"
        },
        "content": {
          "label": "Psychics seem to know their stuff without you giving much information, nice app for horoscopes",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id112250568"
          },
          "name": {
            "label": "vixydixy"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-09-24T13:09:33-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.38.0"
        },
        "id": {
          "label": "11760493812"
        },
        "title": {
          "label": "Terrible"
        },
        "content": {
          "label": "I paid £1 to try it and literally the same moment they took more money. I’m trying to cancel any subscription I have, emailed heard nothing back. I want a refund for the £25.93 they took without my authorization.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1199325376"
          },
          "name": {
            "label": "the L sqaud"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-07-26T10:07:09-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.9.5"
        },
        "id": {
          "label": "7620776739"
        },
        "title": {
          "label": "Lasharie"
        },
        "content": {
          "label": "Is a nice nice game bec u get to know ab your self",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id267901286"
          },
          "name": {
            "label": "MissLake12"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-11-30T08:16:27-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.15.2"
        },
        "id": {
          "label": "8080290725"
        },
        "title": {
          "label": "Waste of time. Free trial full of ads"
        },
        "content": {
          "label": "You can’t use any of the free features without ads popping up. Be careful not to provide your personal info such as date of birth and place of birth.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id439430775"
          },
          "name": {
            "label": "AricAW"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-02T13:09:37-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12137072822"
        },
        "title": {
          "label": "Beware! Unknown money charges!"
        },
        "content": {
          "label": "I spent one euro a while back on a psychic reading via this app..which I then deleted not long after. It did not once mention about a €40 charge extra! I can’t find it anywhere in my subscriptions or even on the app itself. Very sketchy, don’t get involved. Reporting to Apple",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id913723158"
          },
          "name": {
            "label": "uuuuupsetttttttt"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-12-21T15:43:08-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.1.0"
        },
        "id": {
          "label": "6779313893"
        },
        "title": {
          "label": "Avoid"
        },
        "content": {
          "label": "I chose 3 days free trial and it charged my card right away for 9.99/week and to my surprise, it doesn’t let me have full access before I change a free trial to weekly inside app! You charged me for free trial and no full access??????????????????\n9.99 per week?????????",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1483686429"
          },
          "name": {
            "label": "AngelPrin24"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-11-22T08:53:26-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.52.0"
        },
        "id": {
          "label": "11979313841"
        },
        "title": {
          "label": "Nebula"
        },
        "content": {
          "label": "I find this app great, the stuff I read are so true about me & makes me wanna look out for signs & habits",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id950117532"
          },
          "name": {
            "label": "kateee---_"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-04-17T11:29:16-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "4.7.2"
        },
        "id": {
          "label": "7233341149"
        },
        "title": {
          "label": "Good app but..."
        },
        "content": {
          "label": "This is a very good app, I am 14 and I am just a beginner at this sorta stuff and it has really helped me, but I am non binary and when I was putting in my details there was no option for that so I had to pick female which just made me feel horrible",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id333532048"
          },
          "name": {
            "label": "fcurpopups"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-06-12T14:06:02-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "2.5.0"
        },
        "id": {
          "label": "6068226093"
        },
        "title": {
          "label": "Annoying pop up every few seconds makes it unusable"
        },
        "content": {
          "label": "Couldn’t use this app for more than a few minutes. Every few seconds you get this pop up asking if you want to purchase these ‘stickers’. I pressed close but it pops up relentlessly every few seconds. Really annoying. Trying to read my compatibility, have to watch a 30 second ad just to read it, then the pop up occurs and you are thrown out of the compatibility and have to watch another 30 second ad just to get back to where you were, and then the pop up happens again.. and so on.. and so on. You are in an infinite loop where you can't read anything because of the damn pop up! Unusable and annoying!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id504992048"
          },
          "name": {
            "label": "Angry not happy"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-08-15T14:43:43-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.33.0"
        },
        "id": {
          "label": "11614441576"
        },
        "title": {
          "label": "Authorised Pushed Payment Fraud - Subscription trap beware!!!"
        },
        "content": {
          "label": "I’m very angered by the way the App owners have conducted themselves and tricked me into taking recurring payments, when I only authorised a once off payment. Their “advisor” that dealt with my query was incredibly inificient and long winded chats of nothing sandwiches no substantial advice at all and then the audacity to keep on tricking one to believing their terms and conditions are giving them the right and allows them to just unendingly take payments!! I only authorised a once off payment of £4.44 Then they took 2x £22.20 and £34.51!!! I immediately on the day contacted them to rectify it but to no avail… My bank’s legal team is in their case now. Don’t be scammed by them!!! Needless to say I’m not happy and would warn people against this unethical business",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id390496272"
          },
          "name": {
            "label": "FFar1994"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-13T13:11:42-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.55.0"
        },
        "id": {
          "label": "12059849002"
        },
        "title": {
          "label": "Amazing, accurate"
        },
        "content": {
          "label": "Nebula is a great platform to get guidance and clarity on difficult issues. Always amazing and accurate readings that help you make better choices and have advice on difficult situations. Love 🙏🏼",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1645105311"
          },
          "name": {
            "label": "Rev345y"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-04-10T12:51:29-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.12.0"
        },
        "id": {
          "label": "11143537945"
        },
        "title": {
          "label": "AI generated"
        },
        "content": {
          "label": "It seems generalised, inaccurate messages",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1206615525"
          },
          "name": {
            "label": "Fog brains"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-04-19T05:35:18-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.13.0"
        },
        "id": {
          "label": "11176799454"
        },
        "title": {
          "label": "Nebula"
        },
        "content": {
          "label": "Nebula has helped me look at things in a different way \nI’m glad to have my daily horoscope",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id529962060"
          },
          "name": {
            "label": "Katyaty81"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-04-17T09:01:33-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.13.0"
        },
        "id": {
          "label": "11169801921"
        },
        "title": {
          "label": "Great App"
        },
        "content": {
          "label": "Great App lots of interesting resources! Would reccomend 10/10",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1001246823"
          },
          "name": {
            "label": "LittleDoris77"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-04T06:22:12-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12143966289"
        },
        "title": {
          "label": "Keep trying to take money"
        },
        "content": {
          "label": "I wanted to have a look around, I paid the £1 I did not give permission to take anymore money, I am now having attempts to take money for my account and cannot seem to find where to remove my profile to stop this from happening, not great!!!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id114194482"
          },
          "name": {
            "label": "L3852"
          },
          "label": ""
        },
        "updated": {
          "label": "2023-03-05T12:55:33-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.55.0"
        },
        "id": {
          "label": "9683137276"
        },
        "title": {
          "label": "AVOID"
        },
        "content": {
          "label": "Seems just like a scam for gullible people. I got free trial, because I was curious, but it’s truly not worth it. Impossible to cancel the subscription. It just keeps saying that something went wrong. Just stay away.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1045349021"
          },
          "name": {
            "label": "FreyaSelwood"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-01-03T02:50:06-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.1.0"
        },
        "id": {
          "label": "6825542188"
        },
        "title": {
          "label": "Love it!!!"
        },
        "content": {
          "label": "I’ve had this app for a few weeks now and I love it so much! It’s so accurate! I use it mostly for the daily horoscope. However I went on it today and the horoscope wasn’t loading?? I thought it was my wifi but it’s not so I’m not sure if this is a bug in the system or something? Could you help please?:)",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id790365643"
          },
          "name": {
            "label": "krituke"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-07-06T09:16:22-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.9.3"
        },
        "id": {
          "label": "7546147044"
        },
        "title": {
          "label": "Scam"
        },
        "content": {
          "label": "Please do not fall for their scam to buy a report as you will be signed up for a subscription even though you do not have the app.\n\nI received my report and then noticed a payment of $39.99 come off my account for nothing. They ignore all emails completely.\n\nSince I actually did not have the app or any other services from them I was not able to get a refund though apple.\n\nThis app/developer should be investigate by Apple and the apps removed as this company only uses it as a disguise for their financial scam.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "1"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "1"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id34307307"
          },
          "name": {
            "label": "Sackhamish"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-28T13:58:28-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12242579143"
        },
        "title": {
          "label": "Unhappy"
        },
        "content": {
          "label": "Customer support is terrible. They just take random amounts of  money and make it impossible to cancel the subscription. Don’t sign up to this .",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id438745875"
          },
          "name": {
            "label": "Island Girl Lost In The City"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-01-16T07:21:35-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.2.1"
        },
        "id": {
          "label": "6877052958"
        },
        "title": {
          "label": "THIS APP IS A SCAM"
        },
        "content": {
          "label": "I signed up for the 3 day FREE trail and within an hour £48.99 (a yearly subscription fee) had been removed from my bank account. I called apple customer service and the bank to put a block on the payment and they are issuing me a refund. HATE apps like that who try and trick and sneakily get hold of your money!!! DO NOT DOWNLOAD IT'S A WASTE IF TIME AND MONEY. \n\nSHAME ON YOU NEBULA 🤬🤬🤬",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id552698319"
          },
          "name": {
            "label": "AnnaAnchika"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-11-15T06:36:59-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "5.51.0"
        },
        "id": {
          "label": "11952835740"
        },
        "title": {
          "label": "Great"
        },
        "content": {
          "label": "Great application, I’m very pleased how accurate and agile their advisors are.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id165814860"
          },
          "name": {
            "label": "Is king s no d oh ne"
          },
          "label": ""
        },
        "updated": {
          "label": "2023-04-02T11:08:01-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.60.0"
        },
        "id": {
          "label": "9779745191"
        },
        "title": {
          "label": "Charged £39.99 at ‘free trial’"
        },
        "content": {
          "label": "Selected free trial and switched on the notification to remind me when the trial was almost up so I could cancel if I wanted to (which I would have)…but have been charged £39.99 straight away? Not okay",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id131187911"
          },
          "name": {
            "label": "LG3094"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-10T03:53:44-07:00"
        },
        "im:rating": {
          "label": "3"
        },
        "im:version": {
          "label": "5.54.0"
        },
        "id": {
          "label": "12046934197"
        },
        "title": {
          "label": "Mixed"
        },
        "content": {
          "label": "Patrick is amazing to receive readings who makes up for the app issues. It’s expensive to top up and money is taken at times without consent and can be glitchy",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id544320347"
          },
          "name": {
            "label": "kizi168"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-18T13:04:26-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.55.0"
        },
        "id": {
          "label": "12078786394"
        },
        "title": {
          "label": "Love guidance"
        },
        "content": {
          "label": "Love this app",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1181272360"
          },
          "name": {
            "label": "Pjbrazil25"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-04-28T08:15:11-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.15.0"
        },
        "id": {
          "label": "11210013904"
        },
        "title": {
          "label": "FRAUD! Stole £140"
        },
        "content": {
          "label": "This app steals money from your account. Report this Ukrainian scam.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1361745983"
          },
          "name": {
            "label": "hrjfjfjsntj"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-18T18:11:14-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.60.0"
        },
        "id": {
          "label": "12201688704"
        },
        "title": {
          "label": "amazing"
        },
        "content": {
          "label": "love!!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id236315548"
          },
          "name": {
            "label": "Bes684"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-11-27T19:06:50-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.15.2"
        },
        "id": {
          "label": "8071137920"
        },
        "title": {
          "label": "New update - different language"
        },
        "content": {
          "label": "Why is the most recent update showing my weekly horoscope in Spanish?? 🤔🇪🇸",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1256945626"
          },
          "name": {
            "label": "louis12___"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-01-25T23:36:59-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.98.0"
        },
        "id": {
          "label": "10865136726"
        },
        "title": {
          "label": "STAY AWAY FROM THIS APP!"
        },
        "content": {
          "label": "Don’t get this app if you want to keep your money. They regularly take 20 euros out of my bank when I never signed up for that. Do not get this app! If you want to be scammed then download it.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id236808084"
          },
          "name": {
            "label": "Mandjay"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-01-01T13:38:25-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.1.0"
        },
        "id": {
          "label": "6819359654"
        },
        "title": {
          "label": "Excellent"
        },
        "content": {
          "label": "The most accurate Astrology app I have come across. You must make your your birth details are as accurate as possible to get the best from this app.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id542823918"
          },
          "name": {
            "label": "Krimblaran"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-07-03T04:09:06-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "5.25.0"
        },
        "id": {
          "label": "11451509008"
        },
        "title": {
          "label": "Why"
        },
        "content": {
          "label": "I don’t like how nebula has changed I used to be able to see my elements plus see the percentage of my polarity now all that information is gone I don’t like that please bring back the old style before that update immediately cause I am angry about this 😤",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id147406509"
          },
          "name": {
            "label": "Meekteek"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-04-27T02:14:47-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.15.0"
        },
        "id": {
          "label": "11205374904"
        },
        "title": {
          "label": "Scammed 49£ out of my account without giving the 3-day trial"
        },
        "content": {
          "label": "My girlfriend wanted to try the app and we were told there is a 3 day trial before charging us money, as soon as we agreed we were charged 49£",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id775838553"
          },
          "name": {
            "label": "Prettyauro"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-06-26T02:06:27-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.24.0"
        },
        "id": {
          "label": "11424497672"
        },
        "title": {
          "label": "Mrs Macedo"
        },
        "content": {
          "label": "Don't trust, they just want to take your money. less than 24 hours they took £48 from me and didn't tell me anything I asked",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id115576096"
          },
          "name": {
            "label": "ShaunaMatthews"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-11-14T17:27:39-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.51.0"
        },
        "id": {
          "label": "11950898491"
        },
        "title": {
          "label": "Scam!"
        },
        "content": {
          "label": "Clicked to do the 3 day free trial, and was immediately charged £48.99!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id597717712"
          },
          "name": {
            "label": "Madz77798"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-04T02:55:52-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12269225809"
        },
        "title": {
          "label": "Scam"
        },
        "content": {
          "label": "There is no 3 day free trial. Do not be fooled. Hit with a £42.99 charge for the year.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id361478022"
          },
          "name": {
            "label": "DIANA IS DA BEST"
          },
          "label": ""
        },
        "updated": {
          "label": "2019-12-17T00:35:02-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "1.8"
        },
        "id": {
          "label": "5282522525"
        },
        "title": {
          "label": "Nice but phrasing could be different"
        },
        "content": {
          "label": "Lovely app but could be more positive as I don’t have ‘arch enemies’ I have made peace with everyone maybe phrase some parts differently",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id124630351"
          },
          "name": {
            "label": "Bri the bad"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-28T14:36:47-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12242685985"
        },
        "title": {
          "label": "Beware the subscription cancellation instructions do not work"
        },
        "content": {
          "label": "I signed up for a free trial and then tried to cancel the subscription using the instructions on the app, unfortunately this didn’t work and they tried to take a payment from me. I had to contact them in order to get the payment cancelled, to be fair I did get the money back but cancelling the subscription is much harder than it should be and the app misinforms you about how to do this.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id267987533"
          },
          "name": {
            "label": "sekiana"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-29T13:16:09-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12121114107"
        },
        "title": {
          "label": "Didn’t get what i asked for and was charged additionally"
        },
        "content": {
          "label": "1. I have been billed 45.00 and did not sign up after the initial payment ; 2. I requested to know about a spirit animal and paid for that, but instead got a palm reading.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1091120884"
          },
          "name": {
            "label": "mehdi2694"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-06-22T23:26:12-07:00"
        },
        "im:rating": {
          "label": "2"
        },
        "im:version": {
          "label": "5.23.0"
        },
        "id": {
          "label": "11412973690"
        },
        "title": {
          "label": "All a Big Lie!!"
        },
        "content": {
          "label": "Do not believe in this, I spent over $2000 on the app and none of the readings were true",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id128226473"
          },
          "name": {
            "label": "Zakaria3"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-08-23T21:36:12-07:00"
        },
        "im:rating": {
          "label": "2"
        },
        "im:version": {
          "label": "2.7.2"
        },
        "id": {
          "label": "6354416026"
        },
        "title": {
          "label": "It’s not free"
        },
        "content": {
          "label": "It’s not free",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1354878043"
          },
          "name": {
            "label": "Ali1986!"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-01T13:45:27-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12258902521"
        },
        "title": {
          "label": "100% recommend"
        },
        "content": {
          "label": "Spot on with the answers and given me more than I could ever hope for. Created a lot of calm in a strange time for me",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id114508990"
          },
          "name": {
            "label": "muchbunch"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-07-29T07:43:46-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.30.0"
        },
        "id": {
          "label": "11548447798"
        },
        "title": {
          "label": "Beware the subscription trap"
        },
        "content": {
          "label": "Frustrated. I’d followed a link for a reading which was generic in nature and essentially left to a follow your instincts. I’m not trapped in a subscription because the safari experience does not even show an option to unsubscribe and the emails do not contain a link to unsubscribe. Spirituality should never be a stupid tax but it does feel like this. Be cautious on the terms and conditions and make sure you subscribe as soon as you can from any trial to avoid feeling as annoyed as I do right now.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id691752644"
          },
          "name": {
            "label": "snekslks"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-31T11:27:37-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12254102021"
        },
        "title": {
          "label": "DONT DOIT"
        },
        "content": {
          "label": "Impossible to frigging cancel take 39 euros from your bank without your permission I’ve deleted my account and still having issues !! Should be banned",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id171184098"
          },
          "name": {
            "label": "anderson,cjagger"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-06-28T06:37:01-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "2.5.2"
        },
        "id": {
          "label": "6132028029"
        },
        "title": {
          "label": "Great app"
        },
        "content": {
          "label": "I love this app so much it is so cool :)",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id458712985"
          },
          "name": {
            "label": "makemson1"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-06-09T00:30:38-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "2.5.0"
        },
        "id": {
          "label": "6053765073"
        },
        "title": {
          "label": "Not accurate"
        },
        "content": {
          "label": "Not accurate at all it says me and my husband are very incompatible but we’ve been together almost 13 years with 3 children and are very happy",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id929096940"
          },
          "name": {
            "label": "CaptainBitcoin"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-05T04:44:56-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12147721114"
        },
        "title": {
          "label": "£34.00 Taken For Trite Generalistations"
        },
        "content": {
          "label": "Signed up for a €1.00 trial. Got charged £34.00. The ‘readings’ are just generic observations on the same hopes & desires that all humans have, dressed up as insight. \n\nYou could get the same insights reading Freud or Jung. \n\nAn Utter scam, and not even worth the €1.00 trial.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id207872897"
          },
          "name": {
            "label": "Irishlasscb"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-07-08T08:39:45-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.9.3"
        },
        "id": {
          "label": "7553682397"
        },
        "title": {
          "label": "$9.99 a week!!!"
        },
        "content": {
          "label": "Had no idea I was signing up for this. Had a busy few weeks, so was €50 down before I realised. Ridiculous. Cancelled PayPal and emailed customer support, but no reply yet. Be careful…",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id263260402"
          },
          "name": {
            "label": "hopsie2"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-17T08:49:21-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.60.0"
        },
        "id": {
          "label": "12195826694"
        },
        "title": {
          "label": "Excellent app"
        },
        "content": {
          "label": "Very nice concept.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1395949890"
          },
          "name": {
            "label": "KeeleyBell"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-08-01T00:05:21-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.31.0"
        },
        "id": {
          "label": "11558598549"
        },
        "title": {
          "label": "Took money after cancelling subscription!"
        },
        "content": {
          "label": "Absolute scam!! I signed up for the free trial and then cancelled the subscription two days before my free trial ran out, they have proceeded to take €39.99 off m two months in a row now!!!! With nowhere online to even contact them! Absolute scam!! Avoid at all costs!! I want my money back!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id379754947"
          },
          "name": {
            "label": "EmmyY’s"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-02T11:19:33-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12136726747"
        },
        "title": {
          "label": "Avoid"
        },
        "content": {
          "label": "Please avoid creating an account and subscribing to this platform. It is misleading and they try to charge you a subscription fee even when you haven’t subscribed. Avoid at all costs.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1247865110"
          },
          "name": {
            "label": "Gothowitz"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-11-27T07:00:38-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.45.0"
        },
        "id": {
          "label": "9334906882"
        },
        "title": {
          "label": "The best app in the stars"
        },
        "content": {
          "label": "I love the app because it’s written in the stars it’s so cool going through everything there’s to know.\nKeep it up.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1460393266"
          },
          "name": {
            "label": "sienna🎀☃️"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-11-03T16:53:38-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.47.0"
        },
        "id": {
          "label": "11909602045"
        },
        "title": {
          "label": "read the review"
        },
        "content": {
          "label": "tiktok displayed the wrong information about the app and i downloaded it and the tiktok add didnt have anything to do with the actual app.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id428074076"
          },
          "name": {
            "label": "lucíndα"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-02-12T06:06:50-07:00"
        },
        "im:rating": {
          "label": "2"
        },
        "im:version": {
          "label": "4.20.0"
        },
        "id": {
          "label": "8347407621"
        },
        "title": {
          "label": "Very surface level, basic astrology."
        },
        "content": {
          "label": "This app claims to take a ‘deep dive’ into astrology. However, I don’t agree. I think this app only entails beginner, surface level astrology. There’s only information regarding your sun sign, they don’t delve into the other deeper elements such as personal or house placements. This app is only useful to those who are new to astrology and don’t want to delve deep into their full chart.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id125928187"
          },
          "name": {
            "label": "Nottouse"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-10-14T08:48:31-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.41.0"
        },
        "id": {
          "label": "11833527364"
        },
        "title": {
          "label": "Please don’t use unless you want to loose all your money"
        },
        "content": {
          "label": "Please don’t use unless you want to loose all your money. The mechanics of the app is to make you spend more than you can afford. It’s exploiting .",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id976533420"
          },
          "name": {
            "label": "Chomalooo"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-18T04:13:25-07:00"
        },
        "im:rating": {
          "label": "3"
        },
        "im:version": {
          "label": "5.60.0"
        },
        "id": {
          "label": "12198967732"
        },
        "title": {
          "label": "Hi"
        },
        "content": {
          "label": "Very good",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id782853664"
          },
          "name": {
            "label": "LJ05CLK"
          },
          "label": ""
        },
        "updated": {
          "label": "2023-10-14T11:27:35-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.83.0"
        },
        "id": {
          "label": "10474564217"
        },
        "title": {
          "label": "Nebula"
        },
        "content": {
          "label": "Great app!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1216893201"
          },
          "name": {
            "label": "E114343"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-12-11T12:19:46-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.0.0"
        },
        "id": {
          "label": "6742415027"
        },
        "title": {
          "label": "I love this app"
        },
        "content": {
          "label": "I love this App is a great way to find out about the star sign you are and lots of information about it",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id360469812"
          },
          "name": {
            "label": "Kavenior"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-10-24T16:06:36-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.40.0"
        },
        "id": {
          "label": "9218616452"
        },
        "title": {
          "label": "The app is very comprehensive"
        },
        "content": {
          "label": "but it charges me saying there could be astrologists answering my questions, and each question costs you a bit of money. I have paid, not much, but there is no respond since two days from the astrologist. It is quite irresponsible given they used that as the selling point. I will cancel the subscription and it’s a no for me. The interface is also not good enough. cheers.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id468273113"
          },
          "name": {
            "label": "esesswsesss"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-06T10:06:46-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12278703471"
        },
        "title": {
          "label": "Fraud"
        },
        "content": {
          "label": "This app has taken €39 without me subscribing and will not refund the money",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id171397539"
          },
          "name": {
            "label": "lollypop nuber 1"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-06T15:21:05-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.59.0"
        },
        "id": {
          "label": "12153608767"
        },
        "title": {
          "label": "Watch out for charges"
        },
        "content": {
          "label": "Charged twice for subscription in the past. And just charged again even though I had clicked on skip offer.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id565998785"
          },
          "name": {
            "label": "damaged85"
          },
          "label": ""
        },
        "updated": {
          "label": "2019-12-25T17:18:12-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "1.8.3"
        },
        "id": {
          "label": "5319788477"
        },
        "title": {
          "label": "Review"
        },
        "content": {
          "label": "I think this is quiet rite first time for everything I suppose thanks gus",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id101198247"
          },
          "name": {
            "label": "Gemdelucchi"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-06-19T12:48:55-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.23.0"
        },
        "id": {
          "label": "11400164440"
        },
        "title": {
          "label": "Scammers"
        },
        "content": {
          "label": "I signed up for the app and was inundated by emails suggesting other spiritual reports I should try. I clicked on one suggestion thinking it would tell me more, however it immediately took money out of my bank account with no warning. \n\nI wrote to ask for a refund but they are now ignoring my many, many emails. Terrible company!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id188233261"
          },
          "name": {
            "label": "leigh♓️"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-05-25T22:31:14-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.28.0"
        },
        "id": {
          "label": "8708768793"
        },
        "title": {
          "label": "Pisces☀️Capricorn🌙Scorpio⬆️"
        },
        "content": {
          "label": "I love this app I check my horoscope pretty much everyday!! It tells you what sign your planets are in and what house they are. Also has the meaning to read after the ad💖💜🧡💛❤️🪐🧜🏽‍♀️🔮🔥✨",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1340221702"
          },
          "name": {
            "label": "Isa_bella12"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-01-04T06:00:31-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "4.97.0"
        },
        "id": {
          "label": "10783006369"
        },
        "title": {
          "label": "Great app!"
        },
        "content": {
          "label": "Fantastic resources to use as well as very insightful conversations with astrologers! I truly couldn’t recommend Astrologer Elizabeth enough! She is so accurate, very polite. Thank you for the great insights and for helping me on my journey towards healing 🙏💕",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id663004428"
          },
          "name": {
            "label": "Aladfin007"
          },
          "label": ""
        },
        "updated": {
          "label": "2019-05-28T06:35:22-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "1.3"
        },
        "id": {
          "label": "4225201687"
        },
        "title": {
          "label": ":)"
        },
        "content": {
          "label": "Like ^_^",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1349268741"
          },
          "name": {
            "label": "keeleyxkiwi"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-01-10T14:14:11-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.17.0"
        },
        "id": {
          "label": "8226576784"
        },
        "title": {
          "label": "I’m upset"
        },
        "content": {
          "label": "Im trying to put my birthday March 18th 2009 but it’s not letting me and im fully educated in astrology and I know what im doing so im not too young or anything",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id262963282"
          },
          "name": {
            "label": "Hi I'm Lauren"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-07-07T07:09:41-07:00"
        },
        "im:rating": {
          "label": "3"
        },
        "im:version": {
          "label": "4.9.3"
        },
        "id": {
          "label": "7549575418"
        },
        "title": {
          "label": "Too many notifs"
        },
        "content": {
          "label": "Great app but way way way too many notifications. Had to turn them off",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id844437231"
          },
          "name": {
            "label": "your_design_stylist"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-06-12T04:28:34-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.23.0"
        },
        "id": {
          "label": "11372448703"
        },
        "title": {
          "label": "Huge scam"
        },
        "content": {
          "label": "Don’t signup for trial or one off payments. They will take your money on month basis and there is no customer service. It’s a scam run by AI, the readers are also AI, no humans",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id545075626"
          },
          "name": {
            "label": "Angryyy customer 101"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-13T09:37:19-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.59.0"
        },
        "id": {
          "label": "12180164914"
        },
        "title": {
          "label": "Unexpected to charge fee"
        },
        "content": {
          "label": "Follow the guide to cancel the subscription. but didn’t find",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id777927053"
          },
          "name": {
            "label": "thab01"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-04-23T02:23:55-07:00"
        },
        "im:rating": {
          "label": "3"
        },
        "im:version": {
          "label": "4.7.2"
        },
        "id": {
          "label": "7253985745"
        },
        "title": {
          "label": "Review"
        },
        "content": {
          "label": "Thus is shut m, why do I have white writing \n\nSays a lot about your character",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id249952201"
          },
          "name": {
            "label": "Vicko miffed"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-04-22T06:07:46-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.26.0"
        },
        "id": {
          "label": "8594221131"
        },
        "title": {
          "label": "Rippled off"
        },
        "content": {
          "label": "I clicked on the 3 day trail and was charged £8.49",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id41998541"
          },
          "name": {
            "label": "sharynmatilda"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-05T07:08:56-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12148195381"
        },
        "title": {
          "label": "Scammers!"
        },
        "content": {
          "label": "Taken money without my consent, I have no subscriptions (active or non active) so no idea why this has happened - avoid at all costs!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id355105154"
          },
          "name": {
            "label": "Well art"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-11T13:48:13-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.64.0"
        },
        "id": {
          "label": "12299696046"
        },
        "title": {
          "label": "Scam alert"
        },
        "content": {
          "label": "Didn’t opt for a subscription and can’t cancel … furious really",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1101056759"
          },
          "name": {
            "label": "casniolylma"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-06-21T14:27:14-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.9.2"
        },
        "id": {
          "label": "7490953981"
        },
        "title": {
          "label": "Fraud"
        },
        "content": {
          "label": "Careful! It’s a fraud! They charge you weekly even though you ask them to cancel your subscription. Do not give them your bank details!!!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id672876900"
          },
          "name": {
            "label": "bshdghens"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-09-15T12:02:16-07:00"
        },
        "im:rating": {
          "label": "2"
        },
        "im:version": {
          "label": "3.2.0"
        },
        "id": {
          "label": "6432530023"
        },
        "title": {
          "label": "Have to pay for most of it"
        },
        "content": {
          "label": "False advertising. To many in app purchases. Pitty",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id564171716"
          },
          "name": {
            "label": "bexfar83"
          },
          "label": ""
        },
        "updated": {
          "label": "2021-06-09T15:47:45-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.9.2"
        },
        "id": {
          "label": "7446437050"
        },
        "title": {
          "label": "Waste of money!"
        },
        "content": {
          "label": "Set up the free trial which instantly took my money. Asked an astrologer a question and never got a reply. Complete waste of money!!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id966338486"
          },
          "name": {
            "label": "shaquana3333"
          },
          "label": ""
        },
        "updated": {
          "label": "2020-06-28T11:36:32-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "2.5.2"
        },
        "id": {
          "label": "6132958567"
        },
        "title": {
          "label": "My review"
        },
        "content": {
          "label": "I think it’s the best and for it being free and telling you the truth is amazing love it and it’s defo gunna stay on my phone",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1201284557"
          },
          "name": {
            "label": "Thisissounnecessary"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-15T04:45:19-07:00"
        },
        "im:rating": {
          "label": "5"
        },
        "im:version": {
          "label": "5.64.0"
        },
        "id": {
          "label": "12313578845"
        },
        "title": {
          "label": "Amazing"
        },
        "content": {
          "label": "The guides on here such as Charles and luna have been very helpful in making sure i know what I need to be answered and also what will happen in the future. Charles has helped me a lot through a very tough phase in my life",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id563604601"
          },
          "name": {
            "label": "Virgo:-)"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-04-22T15:37:48-07:00"
        },
        "im:rating": {
          "label": "2"
        },
        "im:version": {
          "label": "4.26.0"
        },
        "id": {
          "label": "8595679629"
        },
        "title": {
          "label": "Who Got Fired?"
        },
        "content": {
          "label": "My friend and I used to use this application daily, and boasted about it to everybody we knew. It was extremely accurate, and provided so much interesting information. However, now the daily horoscopes have become general positive quotes and are being recycled through different signs … It’s a shame, please bring back whoever wrote the previous horoscopes :(",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id913228576"
          },
          "name": {
            "label": "dhdklssken"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-29T14:34:22-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.58.0"
        },
        "id": {
          "label": "12121326177"
        },
        "title": {
          "label": "Scammers"
        },
        "content": {
          "label": "I never signed up for the subscription. Now they are trying to charge me €39 for no reason. I don’t even have an account with these people. Complete scam. Stay AWAY",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1471946482"
          },
          "name": {
            "label": "Rambo83…."
          },
          "label": ""
        },
        "updated": {
          "label": "2024-12-12T10:16:56-07:00"
        },
        "im:rating": {
          "label": "4"
        },
        "im:version": {
          "label": "5.55.0"
        },
        "id": {
          "label": "12055619167"
        },
        "title": {
          "label": "Nebula"
        },
        "content": {
          "label": "Was a good experience just hope Now the kind words resonate",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1750350237"
          },
          "name": {
            "label": "Loku Luton"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-01-31T06:54:14-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12253164380"
        },
        "title": {
          "label": "SCAM !!"
        },
        "content": {
          "label": "It’s trying continuously trying to take me 39€ for a subscription I didn’t make and doesn’t let me cancel it and blocked my card for your scam 😡😡!! After this happened to me i came to check the reviews and see the same problem to almost all of the users even years ago and you guys still let it happened, how does apple allow you guys to do this 🤬!!!",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id231997689"
          },
          "name": {
            "label": "DHothi"
          },
          "label": ""
        },
        "updated": {
          "label": "2023-12-11T17:37:30-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.93.0"
        },
        "id": {
          "label": "10683956224"
        },
        "title": {
          "label": "Waste of money and time!"
        },
        "content": {
          "label": "I keep getting messages from SunSofia! When I have no interest in talking to her! Therefore taking some of my credits \n\nCredits have been taken with no proper answers given! \n\nI would like my money back?? But didn’t receive refund! \n\nAdvisors replying back to you after 2 days and saying they need you online to answer questions … as soon you receive a notification and open the app, the advisor has messaged and is no longer showing online! \n\nUnnecessary credits taken with no real questions asked! No breakdown how the funds had been taken for usage of time! \n\nMessaging an adviors telling them when you will be online with credits being taken! \n\nTotal SCAM",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id531732967"
          },
          "name": {
            "label": "Go keep"
          },
          "label": ""
        },
        "updated": {
          "label": "2024-09-23T06:18:25-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.37.0"
        },
        "id": {
          "label": "11755767021"
        },
        "title": {
          "label": "Rubbish"
        },
        "content": {
          "label": "Never received reading after paying money",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id1154282216"
          },
          "name": {
            "label": "The Spiral Mech"
          },
          "label": ""
        },
        "updated": {
          "label": "2025-02-01T10:04:08-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "5.62.0"
        },
        "id": {
          "label": "12258186817"
        },
        "title": {
          "label": "It’s scam"
        },
        "content": {
          "label": "It’s a scam. They will ask you for only $1 and then they will charge you $35 after a few days without your consent.",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      },
      {
        "author": {
          "uri": {
            "label": "https://itunes.apple.com/gb/reviews/id23391"
          },
          "name": {
            "label": "shooshaaa"
          },
          "label": ""
        },
        "updated": {
          "label": "2022-07-15T14:37:06-07:00"
        },
        "im:rating": {
          "label": "1"
        },
        "im:version": {
          "label": "4.33.0"
        },
        "id": {
          "label": "8877769070"
        },
        "title": {
          "label": "FAKE FREE TRIAL WITH ACCOUNT CHARGE, AVOID THIS APP"
        },
        "content": {
          "label": "I am so so unsatisfied with this app, I was offered a 3 day free trial which I hesitantly accepted, and within minutes my account was charged the full annual fee. I cancelled it within minutes and have not been refunded, and also lost access to the subscription of the premium they charged me for. I have been trying to resolve it but there is nowhere on the app to speak to anyone to help. Avoid this app. If I could put 0 stars I would",
          "attributes": {
            "type": "text"
          }
        },
        "link": {
          "attributes": {
            "rel": "related",
            "href": "https://itunes.apple.com/gb/review?id=1459969523&type=Purple%20Software"
          }
        },
        "im:voteSum": {
          "label": "0"
        },
        "im:contentType": {
          "attributes": {
            "term": "Application",
            "label": "Application"
          }
        },
        "im:voteCount": {
          "label": "0"
        }
      }
    ]
  }
}
```

## Metrics
Request:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/metrics?app_id=1459969523' \
  -H 'accept: application/json'
```

Output:
```json
{
  "metrics": {
    "average_rating": 2.01,
    "median_rating": 1,
    "total_reviews": 100,
    "rating_distribution": {
      "rating": [
        3,
        5,
        4,
        2,
        1
      ],
      "count": [
        1,
        17,
        9,
        4,
        69
      ],
      "percentage": [
        1,
        17,
        9,
        4,
        69
      ]
    }
  },
  "insights": {
    "sentiment_counts": {
      "sentiment": [
        "positive",
        "neutral",
        "negative"
      ],
      "count": [
        45,
        7,
        48
      ]
    },
    "negative_review_topics": [
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1
    ],
    "negative_topic_info": [],
    "negative_review_keywords_tfidf": [
      "app",
      "money",
      "subscription",
      "account",
      "taken",
      "scam",
      "cancel",
      "charged",
      "don",
      "sign"
    ],
    "negative_topic_keywords": []
  }
}
```

## Download
Request:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/download?app_id=1459969523' \
  -H 'accept: application/json'
```

Output:
A file

## Visualization

Request:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/visualize?app_id=1459969523' \
  -H 'accept: application/json'
```

Output:
```json
{
  "rating_chart": "https://vega.github.io/editor/#/url/vega-lite/N4Igxg9gdgZglgcxALlANzgUwO4tJKAFzigFcJSBnAdTgBNCALFAZgAY2AacaYsiygAlMiRoVYcAvpO50AhoTl4QUOQFtMKEPMUBaOewCcYMAA5MANgBMc04cxyrMOgHYYAFhYBWTGBhy2AEYrBxAZEDU5ACcAa2VCAE8AB01kEAAjaLDuTChIOhIkVBBCCAgAG2IklABtUHhMcrotKIVCkG5ElK0AR1I5IjhFYjRNGXqsJq1IUiIOkuTUkD6B4mG4UbCAXW4AD2UGqbTWviROofKlgCU2qDOF7rSIKILVcuyQBIPJ5rSZufOhEuWgAwhQAQ8litButNtJAcC0jdTgACAAicEohCicHSpGI0HmABJKGBGJhIloxIQkpRkAB6emjBByAB0CCGjFI6VZcAg9NJ5MiTMwLN05SGmCZXlZVjYrMCrIAVpRCbIFHJKJhCJRlDo5PojCZzNZbPZHM43J4fH4AsFQsg6iATu1kCxuP9xMhAuNnbcil4PeCvYZfS67ih3EHZl6WGH-ShAtG5m6XJIttIgA",
  "sentiment_chart": "https://vega.github.io/editor/#/url/vega-lite/N4Igxg9gdgZglgcxALlANzgUwO4tJKAFzigFcJSBnAdTgBNCALFAZgAY2AacaYsiygAlMiRoVYcAvpO50AhoTl4QUOQFtMKEPMUBaACxyARgE45ADnOmjLW-v0A2BwFZMAdjYxzMGA7YBGczl-NxAZEDU5ACcAa2VCAE8AB01kEGiwMO5MKEg6EiRUHgAbCCjleExiui1KHOINIhBuYkJi1JAAZXq4RvEW5I6oCDUSOWKskCZMRQqsaq1IUiaWuDaOgGEKFanBrQBHUjkiNYU4NE1wwggIYuIklABtUEqFtLqTvubdlK1h0dUExkL3mNTSSx2iV+aUOx1aZwuWRBVTBIBSUTA9TkCE03BgZUi4jSADp-DBvlCOrCTopiIjJABdK5rdpabqfeoAAgAInBKIQonAjKRiNBvgASShgRiYSJaMSEJKUZAAehVFwQcmJCDWjFIRmJcAgKqlMsi6swmt0xTWmHVzmJACY2KTiQArShi2QKOR1QiUZQ6OQGYxmSzWWwsexOVweLw+PyBYKhZDPEAfBr1P6YEVRcbfCFE5zcdGYojY1L+F1sYHpnpfNJQS0I3E8ZZEx0OEuYDFYnEoZyO4k1zigDO9LNpJIQShrc6twsofwmbu98v95AsczDxnSIA"
}
```
