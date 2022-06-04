import json
import jsonschema
from jsonschema import validate

# Describe what kind of json you expect.
Employee_Data_Schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "Emp_id": {"type": "string"},
        "cell phone": {"type": "number"},
        "work phone": {"type": "number"},
        "home phone": {"type": "number"},
        "birth_date": {"type": "string"},
        "govt_id": {"type": "string"},
        "field_day": {"type": "string"}
    },
}

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def JsonValidater(jsonData):
    if "name" not in jsonData:
        return False
    if "Emp_id" not in jsonData:
        return False
    if "cell phone" not in jsonData and "work phone" not in jsonData and "home phone" not in jsonData:
        return False
    if "birth_date" not in jsonData and "govt_id" not in jsonData or "birth_date" in jsonData and "govt_id" in jsonData:
        return False
    # if "Monday" not in "days" and "Tuesday" not in "days" and "Wednesday" not in "days" and "Thursday" not in
    # "days" and "Saturday" not in "days" and "Sunday" not in "days": return False
    #
    # for field in jsonData:
    # if key == "field_day" and value not in day:
    #         return False

    if jsonData.get("field_day") not in day:
        return False
    try:
        validate(instance=jsonData, schema=Employee_Data_Schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


# Convert json to python object.
jsonData = json.loads('{"name": "Jay", "Emp_id": "AI25", "cell phone": 919875463215, "birth_date" : "26-6-01",'
                      '"govt_id" : "r4", "field_day" : "Sunday"}')
# validate it
isValid = JsonValidater(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
    print("\n")
else:
    print(jsonData)
    print("Given JSON data is InValid")
    print("\n")

# Convert json to python object.
jsonData = json.loads(
    '{"name": "Aman", "Emp_id": "AI26", "cell phone": 918546792136, "birth_date" : "9-12-01", "field_day" : "January"}')

# validate it
isValid = JsonValidater(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
    print("\n")
else:
    print(jsonData)
    print("Given JSON data is InValid")
    print("\n")


jsonData = json.loads(
    '{"name": "Jayesh", "Emp_id": "AI24", "cell phone": 91727856421, "birth_date" : "6-2-01", "field_day" : "Sunday"}')

# validate it
# FINAL VALIDATIONS


isValid = JsonValidater(jsonData)
print("The Final Validation of the Given Schema.")

if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
    print("\n")
else:
    print(jsonData)
    print("Given JSON data is InValid")
    print("\n")

"""

        Sends Employee_Data_Schema to JsonValidator

        :type : object

        :properties: dict_values

        :type str: "name", "id" 

        :type int or float : "cellphone", "work phone", "home phone"

        :tags: A list of tags associated with the metric : "weekdays"

        :type tags: list

        :type str: "birth date" or "govt_id"

        :param interval: type - dict: {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

        """
