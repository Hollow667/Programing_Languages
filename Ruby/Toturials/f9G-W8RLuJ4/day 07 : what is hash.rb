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

#sorting by value
hashName2 = {
    'key1' => 3,
    'key2' => 2
    }
hashName2.sort_by(|key, val|val)
