package com.example.controller;

import com.example.model.AppDocument;
import com.example.repository.AppMongoRepoCus;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;
import java.util.Random;

@Controller
public class AppController {

    @Autowired
    AppMongoRepoCus appRepositoryCus;

    //Main Page
    @RequestMapping("main")
    public String mainPage(Model model) {
        model.addAttribute("top100", appRepositoryCus.top100Apps());
        model.addAttribute("popular24", appRepositoryCus.popular24Apps());
        return "MainPage";
    }

    //Top100
    @RequestMapping("/top100")
    public String top100(Model model) {
        model.addAttribute("top100", appRepositoryCus.top100Apps());
        return "top100";
    }

    //Popular24
    @RequestMapping("/{category}")
    public String popular24(@PathVariable String category, Model model) {
        model.addAttribute("top100", appRepositoryCus.top100Apps());
        model.addAttribute("popular24", appRepositoryCus.popular24Apps());
        int startIndex=0;
        if (category.equals("Entertainment")) startIndex=0;
        if (category.equals("Games")) startIndex=1;
        if (category.equals("Health_Fitness")) startIndex=2;
        if (category.equals("News")) startIndex=3;
        if (category.equals("Productivity")) startIndex=4;
        if (category.equals("Photo_Video")) startIndex=5;
        if (category.equals("Music")) startIndex=6;
        if (category.equals("Shopping")) startIndex=7;
        if (category.equals("Social_Networking")) startIndex=8;
        if (category.equals("Utilities")) startIndex=9;
        model.addAttribute("startIndex", startIndex);
        model.addAttribute("category",category);
        return "popular24";
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

    //show all apps
    @RequestMapping("/app")
    public String app(Model model) {
        model.addAttribute("appList", appRepositoryCus.searchByCategory("Books"));
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
        model.addAttribute("appList", appRepositoryCus.searchByCategory(category));
        return "appCategory";
    }

    //show app detail
    @RequestMapping("/app/{category}/{appID}")
    public String showApp(@PathVariable String appID, String category, Model model) {
        AppDocument document = appRepositoryCus.searchById(appID);
        model.addAttribute("app", document);
        List<String> screenShots = document.getiPhone_screenShot();
        List<String> description = document.getDescription();
        List<AppDocument> relatedApps = appRepositoryCus.findRelatedApps(appID);
        List<AppDocument> categoryList = appRepositoryCus.searchByCategory(document.getCategory());
        Random random = new Random();
        while (relatedApps.size() < 5) {
            int index = random.nextInt(categoryList.size());
            if (!relatedApps.contains(categoryList.get(index)))
                relatedApps.add(categoryList.get(index));
        }
        model.addAttribute("relatedAppsList", relatedApps);
        model.addAttribute("description", description);
        if (!screenShots.isEmpty()) {
            model.addAttribute("screenShots", screenShots);
            return "appShow";
        } else
            return "test";
    }

}
