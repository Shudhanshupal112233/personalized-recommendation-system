# Progressive Personalized Recommendation System

This project simulates an AI-powered **progressive personalized recommendation system** for a shopping app.  
It evolves over time based on user interactions — starting from general recommendations and moving toward personalized suggestions based on user behavior.


---

## Project Flow

1. **Cold Start Recommendations**
   - System recommends products based on popularity (popularity_score).
   - Ideal for new users with no interaction history.

2. **Simulate User Clicks**
   - Randomly simulates user clicking 2-3 products from initial recommendations.

3. **Update User Profile**
   - System learns user preferences by extracting tags and categories from clicked products.

4. **Personalized Recommendations**
   - System recommends products based on user profile (preferred tags/categories).
   - Includes 1 popular product to simulate hybrid recommendation logic.

---

##  Technologies Used

- Python 3
- pandas (data handling)
- Optional: matplotlib (for future visualizations)

---



