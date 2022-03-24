using MyFirstApplication;

// See https://aka.ms/new-console-template for more information.
Console.WriteLine("Hello World!");

//The below statement calls a local function
//single line comment
HouseExample();

/*
Multi-line comment
The below statement is a local function. Local functions
are inside of memebers and are private be default. This means
they are specific to that member and can only be called inside that member.
*/
void HouseExample()
{
    House myHouse = new House();
    myHouse.DoorOpenClose();
}