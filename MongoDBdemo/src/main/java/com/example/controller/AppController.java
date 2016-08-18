package com.example.controller;

import com.example.repository.AppMongoRepo;
import com.example.repository.AppMongoRepoCus;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AppController {

    @Autowired
    AppMongoRepo appRepository;

    @Autowired
    AppMongoRepoCus appRepositoryCus;

    @RequestMapping("/")
    public String home(Model model) {
//        model.addAttribute("appList", appRepository.findAll());
        model.addAttribute("category", appRepository.findAll());
        return "home";
    }

    @RequestMapping("/index")
    public String index(Model model) {
        model.addAttribute("appList", appRepository.findAll());
        return "index";
    }

    @RequestMapping("/app/{category}")
    public String AppCategory(@PathVariable String category, Model model) {
        model.addAttribute("appList", appRepositoryCus.searchByCategory(category));
        return "home";
    }

    @RequestMapping("/app/{category}/{appID}")
    public String showApp(@PathVariable String appID, Model model) {
        model.addAttribute("app", appRepositoryCus.searchById(appID));
        model.addAttribute("relatedAppsList", appRepositoryCus.findRelatedApps(appID));
        return "appShow";
    }

}
