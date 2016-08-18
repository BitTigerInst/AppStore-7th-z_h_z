package com.example.repository;

import com.example.model.AppDocument;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

/**
 * Created by Derek on 8/17/16.
 */
public interface AppMongoRepo extends MongoRepository<AppDocument,String> {
    @Override
    List<AppDocument> findAll();

    @Override
    List<AppDocument> findAll(Sort sort);
}
