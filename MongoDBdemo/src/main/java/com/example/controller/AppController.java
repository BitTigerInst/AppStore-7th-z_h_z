package com.example.controller;

import com.example.model.AppDocument;
import com.example.repository.AppMongoRepo;
import com.example.repository.AppMongoRepoCus;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
public class AppController {

    @Autowired
    AppMongoRepo appRepository;

    @Autowired
    AppMongoRepoCus appRepositoryCus;

    @RequestMapping("/test")
    public String home() {
//        model.addAttribute("categoryList", appRepositoryCus.findTop30Apps());
//        model.addAttribute("appList", appRepository.findAll());
//        model.addAttribute("category", appRepository.findAll());
        return "test";
    }

    //sort by averagescore2
    @RequestMapping("/popularApps")
    public String popularApps(Model model) {
//        model.addAttribute("top30", appRepositoryCus.findTop30Apps());
        model.addAttribute("top30", appRepositoryCus.searchForHome());
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
        model.addAttribute("categoryTitle", category);
        model.addAttribute("categoryList", appRepositoryCus.searchPopByCategory(category));
        return "popularAppsCategory";
    }

    //sort by popularscore---release time
    @RequestMapping("/app/top30")
    public String appTop30(Model model) {
        model.addAttribute("top30", appRepositoryCus.findTop30Apps());
        return "top30";
    }

    //show all apps
    @RequestMapping("/app")
    public String app(Model model) {
        model.addAttribute("appList", appRepositoryCus.searchForAll());
        return "app";
    }

    //show all apps from specific category
    @RequestMapping("/app/{category}")
    public String appByCategory(@PathVariable String category, Model model) {
        model.addAttribute("category", category);
        if (category.equals("Food_Drink")) category = "Food & Drink";
        if (category.equals("Health_Fitness")) category = "Health & Fitness";
        if (category.equals("Photo_Video")) category = "Photo & Video";
        if (category.equals("Magazines_Newspapers")) category = "Magazines & Newspapers";
        if (category.equals("Social_Networking")) category = "Social Networking";
        model.addAttribute("categoryTitle", category);
        model.addAttribute("categoryList", appRepositoryCus.searchByCategory(category));
        return "appCategory";
    }

    @RequestMapping("/app/{category}/{appID}")
    public String showApp(@PathVariable String appID, Model model) {
        AppDocument document = appRepositoryCus.searchById(appID);
        model.addAttribute("app", document);
        List<String> screenShots = document.getiPhone_screenShot();
        List<String> description = document.getDescription();
        model.addAttribute("relatedAppsList", appRepositoryCus.findRelatedApps(appID));
        model.addAttribute("description", description);
        if (!screenShots.isEmpty()) {
            model.addAttribute("screenShots", screenShots);
            return "appShow";
        } else
            return "test";
    }

}
