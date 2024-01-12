from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.prompt import Prompt,IntPrompt,FloatPrompt
import time
kingTheme = Theme({"title": "black on rgb(0,255,0)", "sub": "black on rgb(0,255,255)", "wait": "black on rgb(255,0,255)", "link": "rgb(0,255,0) i u", "m": "rgb(255,0,255)"})
console = Console(theme=kingTheme)

def intro(name,author,license,version,year,desc,mail):
  title = Text()
  info = Text()
  title.append('>>'+name, 'title')
  info.append(' ['+author+']; ')
  info.append(license+'; ')
  info.append(mail+'; ', 'link')
  info.append(str(version)+' '+str(year), 'm')
  console.print(title)
  console.print(info)
  console.print('')

def step(str):
  step = Text('>'+str, 'wait')
  console.print(step)
  console.print('')

def outro():
  outro = Text('>>finished', 'title')
  console.print(outro)
  console.print('')

def inputString(str,*defau):
  txt = Text('>'+str, 'sub')
  console.print(txt)
  val = Prompt.ask('',default=defau)
  console.print('')
  return val

def inputInteger(str,*defau):
  txt = Text('>'+str, 'sub')
  console.print(txt)
  val = IntPrompt.ask('',default=defau)
  val = int(round(float(val)))
  console.print('')
  return val

def inputFloat(str,*defau):
  txt = Text('>'+str, 'sub')
  console.print(txt)
  val = FloatPrompt.ask('',default=defau)
  val = float(val)
  console.print('')
  return val

def inputChoices(str,choi,type,*defau):
  if type == 'string':
    txt = Text('>'+str, 'sub')
    console.print(txt)
    val = Prompt.ask('', choices=choi, default=defau)
    console.print('')
    return val
  elif type == 'float':
    txt = Text('>'+str, 'sub')
    console.print(txt)
    val = Prompt.ask('', choices=choi, default=defau)
    val = float(val)
    console.print('')
    return val
  elif type == 'integer':
    txt = Text('>'+str, 'sub')
    console.print(txt)
    val = Prompt.ask('', choices=choi, default=defau)
    val = int(round(float(val)))
    console.print('')
    return val
  elif type == 'boolean':
    txt = Text('>'+str, 'sub')
    console.print(txt)
    val = Prompt.ask('', choices=choi, default=defau)
    console.print('')
    if val == choi[0]:
      val = True
      return val
    else:
      val = False
      return val

intro('kingUI','niklaus iff','MIT License',0.1,2024,'UI toools','dev@niklausiff.ch')
val1 = inputString('wie heissisch du?')
val2 = inputFloat('wie viel grad isch?')
val3 = inputInteger('wie alt bisch du?')
step('wart es gaht grad wieter g')
time.sleep(10)
val4 = inputChoices('chat?',['kira','leya','chica','juve'],'string')
val5 = inputChoices('fuffi?',['4.0','4.5','4.8','5.0'],'float')
val6 = inputChoices('bodycount?',['18','11','2','3'],'integer')
val7 = inputChoices('hesch geld?',['y','n'],'boolean',False)
outro()
