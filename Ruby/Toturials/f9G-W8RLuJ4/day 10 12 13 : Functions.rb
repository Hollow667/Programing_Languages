def func1
  puts "no parameters, no return"
end

def func2(para1)
  puts para1
  puts "no return"
end

def func3
  puts "no parameters"
  return "return a string"
end

def func4(num_para1)
  puts "parameters and return"
  return num_para1
end

func1
func2(1)
puts func3
puts func4(2)
