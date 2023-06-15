// # **Wildlife Preservation:** You're a wildlife conservationist working on a
// # program to track different species in a national park. Each species has its own
// # characteristics and behaviors, such as its diet, typical lifespan, migration
// # patterns, etc. Some species might be predators, others prey. You'll need to
// # create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// # these classes might relate to each other through inheritance.

class Wildlife{
    constructor(diet,lifespan, migrationPattern){
        this.diet = diet
        this.lifespan =lifespan
        this.migrationPattern = migrationPattern
    }
    status(animal){
        this.prey = {}
        if(animal in this.prey){
            return `${animal} is a prey`
        }
        else{
            return `${animal} is a predator`
        }
    }
}

// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.


class Product{
    constructor(name, price, quantity){
        this.price = price
        this.quantity = quantity
        this.name = name
    }
    total(){
        return (this.price * this.quantity)
    } 
}