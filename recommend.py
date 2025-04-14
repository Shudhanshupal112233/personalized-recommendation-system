import pandas as pd
import random as rd


products = pd.read_csv('products.csv')

user_profile= {'tags':[], 'categories':[]}# Empty user profile to start



def start_recmd(products,n=5):
    top_product = products.sort_values(by='popularity_score',ascending=False).head(n)
    print("\n  !!!!! Starting Recommendations  !!!!")
    print(top_product[['product_id' , 'title']])

    return top_product


def user_clicks(recommended_products,nums_clicks=2):
    clicked = recommended_products.sample(nums_clicks)
    print("\n user clicked:")
    print(clicked[['product_id','title']])
    return clicked


def updated_user_profile(clicked_product,user_profile):
    tags =[]
    categories =[]
    for _, row in clicked_product.iterrows():
        tags.extend(row['tags'].split(','))
        categories.append(row['category'].strip())
    
    user_profile['tags'] = list(set(tags))
    user_profile['categories'] = list(set(categories))
    print("\n--- UPDATED USER PROFILE ---")
    print("Preferred tags:", user_profile['tags'])
    print("Liked categories:", user_profile['categories'])
        


def personalized_recommendations(products, user_profile, n=5):
    mask = products['tags'].apply(lambda x: any(tag in x for tag in user_profile['tags'])) | \
           products['category'].apply(lambda x: x.strip() in user_profile['categories'])
    personalized = products[mask].sample(min(n-1, len(products[mask])))
    
    # Add a popular product to keep it hybrid
    popular = products.sort_values(by='popularity_score', ascending=False).head(1)
    
    final_recommendations = pd.concat([personalized, popular]).drop_duplicates().head(n)
    print("\n--Personalized Recommendations ---")
    print(final_recommendations[['product_id', 'title']])


def main():
    recommendation = start_recmd(products)

    clicked= user_clicks(recommendation)
    updated_user_profile(clicked,user_profile)
    personalized_recommendations(products, user_profile)
if __name__ == '__main__':
    main()
