from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class Character:
    def __init__(self, name, gender, description, element):
        self.name = name
        self.gender = gender
        self.description = description
        self.element = element


characters = [
    Character('Amber', 'Female', 'A perky, straightforward girl, who is also the only Outrider of the Knights of Favonius. Her amazing mastery of the glider has made her a three-time winner of the Gliding Champion in Mondstadt. As a rising star within the Knights of Favonius, Amber is always ready for any challenging tasks.', 'Pyro'),
    Character('Diluc', 'Male', 'As the wealthiest gentleman in Mondstadt, the ever-dapper Diluc always presents himself as the epitome of perfection. But behind the courteous visage burns a zealous soul that has sworn to protect Mondstadt at all costs, allowing him to mercilessly vanquish all who threaten his city', 'Pyro'),
    Character('Razor', 'Male', 'Some say he is an orphan raised by wolves. Others say he is a wolf spirit in human form. He is most at home in the wild, fighting with claw and thunder. To this day the wolf boy can be found prowling the forest, where he and his wolf pack hunt to survive using nothing more than their animal instincts.', 'Electro')
]


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def characters_index(request):
    return render(request, 'characters/index.html', {'characters': characters})
