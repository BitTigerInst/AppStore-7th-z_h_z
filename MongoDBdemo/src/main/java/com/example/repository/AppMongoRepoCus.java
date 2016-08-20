package com.example.repository;

import com.example.model.AppDocument;
import com.example.model.popularAppDocument;
import com.example.model.popularAppTop30Document;
import com.example.model.top30Document;
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

    public AppDocument searchById(String id) {
        return mongoTemplate.findOne(new Query(Criteria.where("appID").is(id)), AppDocument.class);
    }

    public List<AppDocument> searchForAll() {
        List<AppDocument> appList = mongoTemplate.findAll(AppDocument.class);
        Collections.sort(appList, new Comparator<AppDocument>() {
            @Override
            public int compare(AppDocument o1, AppDocument o2) {
                return o1.getName().compareTo(o2.getName());
            }
        });
        return appList;
    }
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

    public List<popularAppTop30Document> searchForHome() {
        return mongoTemplate.findAll(popularAppTop30Document.class);
    }

    public List<popularAppDocument> searchPopByCategory(String category) {
        return mongoTemplate.find(new Query(Criteria.where("category").is(category)), popularAppDocument.class);
    }

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

//    public List<AppDocument> searchByName(String name) {
//        return mongoTemplate.find(new Query(Criteria.where("name").regex(name, "i")), AppDocument.class);
//    }

    //sort by release time
    public List<top30Document> findTop30Apps() {
        return mongoTemplate.findAll(top30Document.class);
    }
}
