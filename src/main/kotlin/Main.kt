import org.w3c.dom.ranges.Range
import java.sql.Time

fun main() {
    var storyOne = AncestralStories(120, "independence", 16..20)
    storyOne.story("Joy", "This is a story of a young lady from the home of...")
    storyOne.translator("joy", "English")
    storyOne.translator("joy", "Kiswahili")
}
class AncestralStories(var length:Int, var moralLesson:String, var agegroup:IntRange){
    var stories = mutableListOf<String>()
    val storyLanguage = "English"
    fun story(title:String, story:String){
        if(story in stories){
            println("The story with the tittle ${title} is already in the system")
        }
        else{
            stories.add(story)
            println("story added successfully ${stories}")
        }
    }
    fun translator(story: String, language:String){
        if(language == storyLanguage){
            println("Here is the story with the title ${story}")
        }
        else{
            println("Story titled ${story} has been translated from ${storyLanguage} to ${language}")
        }
    }
}

//class Recipe(){
//    var meals = listOf<String>()
//    var ingredients = mutableListOf<String>()
//    var prep_time = listOf<String>() }
//    var nutritional_info = {}
//    fun addRecipe(meal:String, ingredients:List<String>, prep_time_in_minutes:String){
//        if (meal in meal){
//            println("${meal} is in the App already")
//        }
//        else{
//            ingredients = (ingredients)
//        }
//    }
//}


