package com.example.controller;

import com.example.repository.AppMongoRepo;
import com.example.repository.AppMongoRepoCus;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Controller
public class AppController {

    @Autowired
    AppMongoRepo appRepository;

    @Autowired
    AppMongoRepoCus appRepositoryCus;

    @RequestMapping("/test")
    public String home(Model model) {
        model.addAttribute("top30", appRepositoryCus.findTop30Apps());
//        model.addAttribute("appList", appRepository.findAll());
//        model.addAttribute("category", appRepository.findAll());
        return "test";
    }

    @RequestMapping("/popularApps")
    public String popularApps(Model model) {
        List<String> categories = new ArrayList<String>(Arrays.asList(
                "Books",
                "Business",
                "Catalogs",
                "Education",
                "Entertainment",
                "Finance",
                "Food_Drink",
                "Games",
                "Health_Fitness",
                "Lifestyle",
                "News",
                "Productivity",
                "Photo_Video",
                "Magazines_Newspapers",
                "Music",
                "Travel",
                "Reference",
                "Sports",
                "Medical",
                "Social_Networking",
                "Utilities",
                "Shopping",
                "Navigation",
                "Weather"));
        model.addAttribute("top30", appRepositoryCus.findTop30Apps());
        model.addAttribute("categoryList", categories);
        model.addAttribute("categoryDetails", appRepositoryCus.searchByCategory());
        return "popularApps";
    }

    @RequestMapping("/popularApps/{category}")
    public String popularAppsByCategory(@PathVariable String category, Model model) {
        model.addAttribute("category", category);
        if (category.equals("Food_Drink")) category = "Food & Drink";
        if (category.equals("Health_Fitness")) category = "Health & Fitness";
        if (category.equals("Photo_Video")) category = "Photo & Video";
        if (category.equals("Magazines_Newspapers")) category = "Magazines & Newspapers";
        if (category.equals("Social_Networking")) category = "Social Networking";
        model.addAttribute("categoryList", appRepositoryCus.searchByCategory(category));
        return "test";
    }

    @RequestMapping("/app/{category}/{appID}")
    public String showApp(@PathVariable String appID, Model model) {
        model.addAttribute("app", appRepositoryCus.searchById(appID));
        model.addAttribute("relatedAppsList", appRepositoryCus.findRelatedApps(appID));
        return "appShow";
    }

}
