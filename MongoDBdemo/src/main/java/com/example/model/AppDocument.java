package com.example.model;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.Date;
import java.util.List;

/**
 * Created by Derek on 8/17/16.
 */
@Document(collection = "appStore")
@Data
public class AppDocument {
    @Id
    String id;
    String appID;
    String name;
    String category;
    List<String> iPad_screenShot;
    List<String> iPhone_screenShot;
    double averageScore1;
    double averageScore2;
    double popularScore;
    List<String> description;
    String allRating;
    String currentRating;
    String url;
    Long currentRatingCount;
    Long allRatingCount;
    Date lauch_time;
    double aggregateRating;
    double currentRatingValue;
    double allRatingValue;
    List<String> related_app;

    public AppDocument() {
    }

    public List<String> getRelated_app() {
        return related_app;
    }

}
