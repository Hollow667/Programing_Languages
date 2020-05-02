##
hashName = {
    "key1" => "val1",
    "key2" => "val2"
}
puts hashName["key1"]
hashName["key2"] = "new val2"
puts hashName["key2"]

hashName = Hash.new
hashName["key1"]="val new1"
hashName["key2"]="val new2"
puts hashName
