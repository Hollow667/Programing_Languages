class Animal
attr_accessor :name, :age, :trait
end

class Dog < Animal
end

class Cat < Animal
end

class Fish < Animal
attr_accessor :type
end

fish = Fish.new
fish.name = "Nemo"
fish.age = 3
fish.type = "goldfish"

puts fish.name
puts fish.age
puts fish.type