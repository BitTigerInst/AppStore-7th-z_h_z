package com.example.model;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.Date;
import java.util.List;

/**
 * Created by Derek on 8/17/16.
 */
@Document(collection = "top100")
@Data
public class top100Document {
    @Id
    String id;
    String appID;
    String name;
    String category;
    String url;


    public top100Document() {
    }


}
