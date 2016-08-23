package com.example.repository;

import com.example.model.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * Created by Derek on 8/17/16.
 */
@Repository
public class AppMongoRepoCus {
    @Autowired
    MongoTemplate mongoTemplate;


    //Find Top100 Apps
    //Sort by release time
    public List<top100Document> top100Apps() {
        return mongoTemplate.findAll(top100Document.class);
    }

    //Find Popular24 Apps for each category
    //Sort by rating values and rating count

    public List<popularAppTop24Document> popular24Apps() {
        return mongoTemplate.findAll(popularAppTop24Document.class);
    }

    //Find Popular Apps for each category
    //Sort by rating values and rating count
    public List<popularAppDocument> searchPopByCategory(String category) {
        return mongoTemplate.find(new Query(Criteria.where("category").is(category)), popularAppDocument.class);
    }

    //Show All Apps By Category
    public List<AppDocument> searchByCategory(String category) {
        List<AppDocument> appList = mongoTemplate.find(new Query(Criteria.where("category").is(category)), AppDocument.class);
        Collections.sort(appList, new Comparator<AppDocument>() {
            @Override
            public int compare(AppDocument o1, AppDocument o2) {
                return o1.getName().compareTo(o2.getName());
            }
        });
        return appList;
    }

    public AppDocument searchById(String id) {
        return mongoTemplate.findOne(new Query(Criteria.where("appID").is(id)), AppDocument.class);
    }

    //find related apps
    public List<AppDocument> findRelatedApps(String id) {
        AppDocument appDocument = mongoTemplate.findOne(new Query(Criteria.where("appID").is(id)), AppDocument.class);
        List<String> related_appID = appDocument.getRelated_app();
        List<AppDocument> related_App = new ArrayList<AppDocument>();
        for (String temp : related_appID
                ) {
            AppDocument tempDocument = mongoTemplate.findOne(new Query(Criteria.where("appID").is(temp)), AppDocument.class);
            if (tempDocument != null)
                related_App.add(tempDocument);
        }
        return related_App;
    }
}
