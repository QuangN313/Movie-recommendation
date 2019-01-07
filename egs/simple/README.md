# Kết quả recommend trên tập ua.test sử dụng Simple Recommender

* Thực hiện đánh giá trên tập gồm 9430 đánh giá

* Rating >= 3: user like item (Label 1)
* Rating < 3: user dislike    (Label 0)

```
                precision    recall  f1-score   support

           0       0.20      0.88      0.32      1537
           1       0.93      0.30      0.46      7893

   micro avg       0.40      0.40      0.40      9430
   macro avg       0.56      0.59      0.39      9430
weighted avg       0.81      0.40      0.44      9430

Matrix: 
[[1359  178]
 [5487 2406]] 
 
```