from distutils import command
import discord
from discord.ext import commands
from discord_components import *
import requests
from pycoingecko import CoinGeckoAPI
import json
from pretty_help import PrettyHelp
import pandas as pd
import os
import time
from typing import KeysView
from requests import delete
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from discord.ext import commands, tasks
from discord_components import *
from discord_buttons_plugin import *
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
import settings

os.chdir(settings.PATH)

cg = CoinGeckoAPI()
client = commands.Bot(command_prefix = '!',help_command=PrettyHelp())
client.remove_command("help")
buttons = ButtonsClient(client)

@client.event
async def on_ready():
    print('bot hazir')
      
@client.command()
async def price(ctx, coin1:str):
   for sayfa in range(5):
    data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page="+str(sayfa)+"&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d", headers={"accept":"application/json"}).text
    data = json.loads(data)

    for giris in data :  
         if giris["symbol"] == coin1.lower():
           list24h=str("1 hour   :`%")+str(round(giris["price_change_percentage_1h_in_currency"],2))+str("`")+"\n"+str("24 hour :`%")+str(round(giris["price_change_percentage_24h_in_currency"],2))+str("`")+"\n"+str("7 days   :`%")+str(round(giris["price_change_percentage_7d_in_currency"],2))+str("`")+"\n"+str("30 days  :`%")+str(round(giris["price_change_percentage_30d_in_currency"],2))+str("`")
           listmcap =str(giris["name"])+str(" Price : ")+str(giris["current_price"])+str(" $")+"\n"+str("MarketCap :`")+str("{:,}".format(giris["market_cap"]))+str("` $$$")+"\n"+str("MarketCap Rank :# `")+str(giris["market_cap_rank"])+str("`")+"\n"+str("TotalVolume :`")+str("{:,}".format(giris["total_volume"]))+str("` USD")+"\n"+str("MaxSuply :`")+str(giris["max_supply"])+str("` ")+str(coin1.upper())+"\n"+str("TotalSupply :`")+str(giris["total_supply"])+str(" `")+str(coin1.upper())+"\n"+str("CirculatingSupply :`")+str("{:,}".format(giris["circulating_supply"]))+str(" `")+str(coin1.upper())
           coin1=giris["name"]+" ("+giris["symbol"]+")"
           embed = discord.Embed(title=coin1+" price : ",description=listmcap,color=0x9208ea,Timestamp=ctx.message.created_at)
           embed.set_thumbnail(url=giris["image"])     
           embed.add_field(name="Price changes :",value=list24h,inline=True)
           embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
           await ctx.send(embed=embed)
           print(giris["current_price"])
           return
         if coin1.lower() == "magic":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cosmic-universe-magic-token&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["cosmic-universe-magic-token"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Magic Price : ")+str(data1["cosmic-universe-magic-token"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str(data1["cosmic-universe-magic-token"]["usd_market_cap"])+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["cosmic-universe-magic-token"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("100,000,000`Magic")
          embed = discord.Embed(title="Magic"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/19313/large/13037.png?1635025843")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return
         if coin1.lower() == "iris":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iris-token-2&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["iris-token-2"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Iris Price : ")+str(data1["iris-token-2"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str(data1["iris-token-2"]["usd_market_cap"])+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["iris-token-2"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("1,000,000`Iris")
          embed = discord.Embed(title="Iris"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/930167661562855484/945028060468609124/IRIS_Green.png")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return
         if coin1 == "lumen":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tranquility-city&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["tranquility-city"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Lumen Price : ")+str(data1["tranquility-city"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str(data1["tranquility-city"]["usd_market_cap"])+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["tranquility-city"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("15,000,000`Lumen")
          embed = discord.Embed(title="Lumen"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/21813/large/LVuXhMQ.png?1640070267")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return
         if coin1.lower() == "viper":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=viper&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["viper"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Viper Price : ")+str(data1["viper"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str("{:,}".format(round(data1["viper"]["usd_market_cap"],2)))+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["viper"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("500,000,000`viper")
          embed = discord.Embed(title="Viper"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/15305/large/0c4b902b40f14db918f4500956386414ab7ebcfe.jpeg?1620371961")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return
         if coin1 == "algb":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=algebra&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["algebra"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Algebra Price : ")+str(data1["algebra"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str("{:,}".format(round(data1["algebra"]["usd_market_cap"],2)))+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["algebra"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("500,000,000`Algebra")
          embed = discord.Embed(title="Algebra"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/19580/large/13211.png?1635469023")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return 
         if coin1.lower() == "roy":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=crypto-royale&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["crypto-royale"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Crypto Royale Price : ")+str(data1["crypto-royale"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str("{:,}".format(round(data1["crypto-royale"]["usd_market_cap"],2)))+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["crypto-royale"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("400,000,000`Crypto Royale")
          embed = discord.Embed(title="Algebra"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/20668/large/ROY_logo_new_design_small.png?1637547627")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return 
         if coin1.lower() == "ape":
          data1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=harmon-ape&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers={"accept":"application/json"}).text
          data1 = json.loads(data1)
          listmagic=str("24 hour   :`%")+str("{:,}".format(round(data1["harmon-ape"]["usd_24h_change"],2)))+str("`")
          listmmagic=str("Harmon Ape : ")+str(data1["harmon-ape"]["usd"])+str(" $")+"\n"+str("MarketCap :`")+str("{:,}".format(round(data1["harmon-ape"]["usd_market_cap"],2)))+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(data1["harmon-ape"]["usd_24h_vol"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("999,000,000`Harmon Ape")
          embed = discord.Embed(title="Harmon Ape"+" price :",description=listmmagic,color=0x9208ea,Timestamp=ctx.message.created_at)
          embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/22152/large/6183fb2d3f24f48afa4be19e_harmonapelogo.png?1640939670")     
          embed.add_field(name="Price changes :",value=listmagic,inline=True)
          embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)     
          return 
         if coin1.lower()== "plts":
            price_plts = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xd32858211fcefd0be0dd3fd6d069c3e821e0aef3", headers={"accept":"application/json"}).text
            price_plts= json.loads(price_plts)   
            listplts=str("24 hour   :`%")+str("{:,}".format(round(price_plts['pairs'][0][ "priceChange"]["h24"],2)))+str("`")+str("\n")+str("6 hour   :`%")+str("{:,}".format(round(price_plts['pairs'][0][ "priceChange"]["h6"],2)))+str("`")+str("\n")+str("1 hour   :`%")+str("{:,}".format(round(price_plts['pairs'][0][ "priceChange"]["h1"],2)))+str("`")
            listplts1=str("Plutus Price : ")+str(price_plts['pairs'][0]["priceUsd"])+str(" $")+"\n"+str("MarketCap :`")+str("{:,}".format(round(price_plts['pairs'][0]["fdv"],2)))+str("` $$$")+"\n"+str("TotalVolume :`")+str("{:,}".format(round(price_plts['pairs'][0]["volume"]["h24"],2)))+str("`")+str(" USD")+"\n"+str("MaxSuply :`")+str("3,000,000`Plutus")
            embed = discord.Embed(title="PLTS"+" price :",description=listplts1,color=0x9208ea,Timestamp=ctx.message.created_at)
            embed.set_thumbnail(url="https://plutus.hermesdefi.io/plutus-logo.png")     
            embed.add_field(name="Price changes :",value=listplts,inline=True)
            embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed) 
            return
@client.command()
async def social(ctx):
	await buttons.send(
		content="Official Social Media Links :",
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Link,
					label = "Twitter",
					url = "https://twitter.com/hermesdefi",
				),

				Button(
					style = ButtonType().Link,
					label = "Reddit",
					url = "https://www.reddit.com/r/HermesDefi/"

				),
				Button(
					style = ButtonType().Link,
					label = "Telegram",
					url = "https://t.me/hermesdefinance",
				),
				Button(
					style = ButtonType().Link,
					label = "YouTube",
					url = "https://www.youtube.com/channel/UCnLWipB915XYPHMmMZcsnag",
				),
			])
		]
	)              

@client.command()
async def links(ctx):
  await ctx.send("Official Hermes Links :",components=[
    [Button(style=ButtonStyle.URL,label="Website",url="https://www.hermesdefi.io"),
    Button(style=ButtonStyle.URL,label="Docs",url="https://hermes-defi.gitbook.io/plutus/"),
    Button(style=ButtonStyle.URL,label="Grant",url="https://talk.harmony.one/t/hermes-defi-investment/12405/5"),
    Button(style=ButtonStyle.URL,label="Github",url="https://github.com/Hermes-defi"),
    Button(style=ButtonStyle.URL,label="Medium",url="https://medium.com/@HermesDefi")],
    [Button(style=ButtonStyle.URL,label="Wiki",url="https://wiki.hermesdefi.io")],
  ]
  )  

@client.command()
async def help(ctx,*,args=None):

    if args == "tipbot":
      embed = discord.Embed(title="TipBot Commands :",description="Help Command for Tip Bot ",color=0x97ffff)
      embed.add_field(name="`!wallet`",value="Shows the PLTS in your wallet",inline=True)
      embed.add_field(name="`!withdraw (Your Harmony wallet address) (The amount of PLTS to withdraw)`",value="This command may take a little longer to complete (about 1 minute).\nExample : !withdraw 0x1234...00 50 (send 50 PLTS to 0x1234...00 wallet addres",inline=False)
      embed.add_field(name="`!tip (Discord name or ID) (The amount of PLTS)`",value="Sends PLTS to the specified wallet (Only the team can use this command).",inline=False)
      await ctx.send(embed=embed)
      return
    elif args == "memobot".lower():
      
      embed = discord.Embed(title="MemoBot Commands :",description="Help Command for Memo Bot ",color=0x97ffff)
      embed.add_field(name="`!note (Discord name or ID)`",value="Shows notes about person x",inline=True)
      embed.add_field(name="`!update (Discord name or ID)`",value="Update notes about person x",inline=True)
      await ctx.send(embed=embed) 
      return 
    elif args == None:
      await ctx.send("Please enter the code for one of the bots below\n`hermesbot` , `tipbot` , `pricebot` , `memobot`\nEx : !help hermesbot")  
    elif args == "pricebot".lower():
      embed = discord.Embed(title="PriceBot Commands :",description="Help Command for Price Bot ",color=0x97ffff)        
      embed.add_field(name="`!Price (Symbol)`",value="Shows info about coin",inline=True)
      
      await ctx.send(embed=embed) 
      return   
    elif args == "hermesbot".lower():
      embed = discord.Embed(title="HermesBot Commands :",description="Help Command for Hermes Bot ",color=0x97ffff) 
      embed.add_field(name="`!links`",value="Shows social media links",inline=False)
      embed.add_field(name="`!contract (Symbol)`",value="Shows contract adress",inline=False)
      embed.add_field(name="`!faucet (Network)`",value="Shows faucet link",inline=True)
      embed.add_field(name="`!bridge (iris or harmony)`",value="Shows bridge links",inline=False)
      embed.add_field(name="`!currentprice`",value="Shows what the HRMS launch price will be",inline=False)
      embed.add_field(name="`!tvl`",value="Shows the total amount of money in HermesDefi",inline=False)
      await ctx.send(embed=embed)   
    else :
      await ctx.send("Please enter the code for one of the bots below\n`hermesbot` , `tipbot` , `pricebot` , `memobot`\nEx : !help hermesbot") 
     
@client.command()
async def contract(ctx,contrat:str):
  for liste in contrat:
    if contrat=="iris":
      await ctx.send("IRIS Harmony Contract : `0x85fd5f8dbd0c9ef1806e6c7d4b787d438621c1dc`\nIRIS Polygon Contract : `0xdab35042e63e93cc8556c9bae482e5415b5ac4b1`")
      return
    if contrat=="plts":
      await ctx.send("PLTS Harmony Contract : `0xd32858211fcefd0be0dd3fd6d069c3e821e0aef3` (%4 slippage)")
      return
    if contrat=="lp":
      await ctx.send("PLUTUS / 1DAI contract: `0xbbdcb6445b06df78db0b67ea3a0a03e16dc59936`\nIRIS / WONE contract: `0x54c59cc0ad2ec1de3c5b7057d900d306f16453ef`")    
      return
    
@client.command()
async def faucet(ctx,fau:str):
  for liste1 in fau:
    if fau== "harmony":
      await ctx.send("https://stakely.io/faucet/harmony-one")
      return
    if fau== "matic":
      await ctx.send("https://stakely.io/faucet/polygon-matic")
      return
    if fau=="bsc" :
      await ctx.send("https://stakely.io/faucet/bsc-chain-bnb")   

@client.command()
async def bridge(ctx,br:str):
  for liste2 in br:
    if br=="harmony":
      await ctx.send("https://bridge.harmony.one/one")
      return
    if br=="iris" :
      await ctx.send("https://anyswap.exchange/#/bridge")
      return 

@client.command()
async def tvl(ctx):
  sheet_id = "1mVKGZvjQubqxeaCxpBVMVaDMDoCVSEN8"
  df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
  total_tvl = df["$1,250,000"].values.tolist()
  await ctx.send(total_tvl[41] + str(" $"))
  return

@client.command()
async def wonebank(ctx):
  sheet_id = "1mVKGZvjQubqxeaCxpBVMVaDMDoCVSEN8"
  df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
  wone_bank = df["Unnamed: 15"].values.tolist()
  await ctx.send(wone_bank[18])
  return

@client.command()
async def currentprice(ctx):
  price_plts = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xd32858211fcefd0be0dd3fd6d069c3e821e0aef3", headers={"accept":"application/json"}).text
  price_plts= json.loads(price_plts)
  sheet_id = "1mVKGZvjQubqxeaCxpBVMVaDMDoCVSEN8"
  df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
  current_price = df["Unnamed: 14"].values.tolist()
  current_price = current_price[39].replace("$","")
  x = float(current_price) * 0.5603998308
  xr = float(x) / float(price_plts['pairs'][0]["priceUsd"]) 
  x = str("{:,}".format(round(x,3)))
  xr = str("{:,}".format(round(xr,2)))
  y = float(current_price) * 0.6610169492
  yr =float(y) / float(price_plts['pairs'][0]["priceUsd"])
  y = str("{:,}".format(round(y,3)))
  yr = str("{:,}".format(round(yr,2)))
  await ctx.send(f"0.56 conversion PLTS -> ~{xr}x increase ({x}$)\n0.66 conversion PLTS -> ~{yr}x increase ({y}$)\n\nHRMS Price :{current_price}$")
  return

@client.command()
async def goodbot(ctx):
  await ctx.send(f"Thank you {ctx.author} 💙")
  return

@client.command()
async def rpc(ctx):
  await ctx.send("The Hermes RPC is live! Follow this guide to add it to MetaMask!\nhttps://hermes-defi.gitbook.io/plutus/bonus/hermes-defi-rpc\n\nNetwork Name: Hermes DeFi RPC (beta)\nRPC URL: https://rpc.hermesdefi.io/\nChain ID: 1666600000\nCurrency Symbol: ONE\nBlock Explorer: https://explorer.harmony.one/")

@client.event
async def on_message(message):
    if(message.channel.id==settings.EVENT_CHANNEL_ID) :
        await message.add_reaction("<:Plutus:910661422432784384>")
        return
    await client.process_commands(message)    

async def get_bank_data():
    with open("banka.json", "r") as f:
        users = json.load(f)
    return users

@client.command()
async def wallet(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    users1 = users[str(user)]["wallet"]
    users1 = ("{:,}".format(round(users1,2)))
    await ctx.send(f"{ctx.author.mention} has {users1} PLTS in wallet")

@commands.has_role(settings.ADMIN_ROLE)
@client.command()
async def tip(ctx,name : discord.Member,bal:float):
    await open_account(name)
    user = name
    users = await get_bank_data()
    earnings = bal
    await ctx.send(f"I sent {bal} PLTS to {name.mention} wallet .") 
    users[str(user)]["wallet"] += earnings
    with open("banka.json", "w") as f:
        json.dump(users,f)

@client.command()
async def withdraw(ctx,adres:str,miktar:float):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    users1 = users[str(user)]["wallet"]
    
    if miktar > users1 :
        await ctx.send (":)")
    elif miktar == 0 :
        await ctx.send("Please enter a valid amount")
    elif users1 == 0 :
        await ctx.send("You have a 0 PLTS :/")    
    else : 
        users[str(user)]["wallet"] -= miktar
        with open("banka.json", "w") as f:
           json.dump(users,f)
        newb = users[str(user)]["wallet"]   
        await ctx.send(f"New ballance : {newb} PLTS")
        await ctx.send("Please wait , this process may take a long time (up to an estimated 1 minute)")
        
        opt = webdriver.ChromeOptions()
        opt.add_extension(settings.EXTENSION_PATH)
        time.sleep(2)
        driver = webdriver.Chrome(chrome_options=opt) 
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close() 
        driver.switch_to.window(driver.window_handles[0])
        driver.minimize_window()  
        
        time.sleep(1)
        elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div/button').click()
        time.sleep(1)
        elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)
        elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(1)
        
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_1)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_2)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_3)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[4]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_4)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[5]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_5)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[6]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_6)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[7]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_7)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[8]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_8)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[9]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_9)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[10]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_10)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[11]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_11)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[12]/div[1]/div/input'))).send_keys(settings.METAMASK_WORD_12)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[1]/div/input'))).send_keys(settings.METAMASK_PASSWORD)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[2]/div/input'))).send_keys(settings.METAMASK_PASSWORD)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input'))).click()
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/button'))).click()
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/button'))).click()
        
        driver.get(f"chrome-extension://{settings.CHROME_EXTENSION}/home.html#settings/networks/add-network")
        time.sleep(1)
        
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input'))).send_keys("Harmony Mainnet")
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input'))).send_keys("https://api.harmony.one")
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input'))).send_keys("1666600000")
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input'))).send_keys("ONE")
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input'))).send_keys("https://explorer.harmony.one/")
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'))).click()
        
        driver.get(F"chrome-extension://{settings.CHROME_EXTENSION}/home.html#import-token")
        time.sleep(1)
        
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div/input'))).send_keys("0xd32858211fcefd0be0dd3fd6d069c3e821e0aef3")
        time.sleep(1)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/footer/button'))).click()
        time.sleep(1)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/footer/button[2]'))).click()
        time.sleep(1)
        driver.get(f"chrome-extension://{settings.CHROME_EXTENSION}/home.html#send")
        time.sleep(1)
        
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/input'))).send_keys(adres)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[3]/div[2]/div[1]/div/div/div[1]/input'))).send_keys(miktar)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys(Keys.BACK_SPACE)
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div[2]/input'))).send_keys("32")
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/footer/button[2]'))).click()
        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div[3]/footer/button[2]'))).click()
        time.sleep(1)
        driver.close()
        await ctx.send(f"{ctx.author.mention} Completed 🤖")
                        
async def open_account(user):
    users = await get_bank_data()

    if str(user) in users:
        return False
    else:
        users[str(user)]  = {}
        users[str(user)]["wallet"] = 0
        users[str(user)]["bank"] = 0

    with open ("banka.json", "w") as f:
        json.dump(users, f)
    return True

async def get_memo_data():

    with open("kullanici.json", "r") as f:
        users = json.load(f)
    return users

@commands.has_role(settings.MODERATOR_ROLE)
@client.command()
async def note(ctx,name2 : discord.Member):
    await open_account(ctx.author)
    user = name2
    users = await get_memo_data()
    users1 = users[str(user)]["wallet"]
    await ctx.send(f"{name2.name} = '{users1}'")

@commands.has_role(settings.ADMIN_ROLE)
@client.command()
async def update(ctx,name1 : discord.Member,*,args):
    await open_account(name1)
    user = name1
    users = await get_memo_data()
    earnings = args
    users[str(user)]["wallet"] = str(earnings)
    await ctx.send (f"{name1.name} note has been updated to `{args}`")
    with open("kullanici.json", "w") as f:
        json.dump(users,f)
                        
async def open_account(user):
    users = await get_memo_data()

    if str(user) in users:
        return False
    else:
        users[str(user)]  = {}
        users[str(user)]["wallet"] = ""
        

    with open ("kullanici.json", "w") as f:
        json.dump(users, f)
    return True

@client.command()
async def audit(ctx):
  urlpage = 'https://www.certik.com/projects/hermes-defi'
  page = requests.get(urlpage)
  soup = BeautifulSoup(page.content, 'html.parser')
  soup = soup.text
  soup = soup.split(' ')
  soup = soup[84]
  soup = soup.replace("Project","")
  embed = discord.Embed(title="HermesDefi Audit",description=f"Hermes Defi audit is in progress - `{soup}`",url=urlpage,color=0x97ffff)
  await ctx.send(embed=embed)

@client.command()
async def official(ctx):
    
    embed = discord.Embed(title="Official Links :",description="💻 Website : https://plutus.hermesdefi.io/app \n 📰 Whitepaper : https://hermes-defi.gitbook.io/plutus/bonus/hermes-defi-whitepaper-v2 \n 🗺️ Roadmap : https://hermes-defi.gitbook.io/the-hermes-protocol/the-hermes-protocol/roadmap \n <:Hermes:942977539754848307> Hermes Docs : https://docs.hermesdefi.io \n <:Plutus:910661422432784384> Plutus Docs : https://hermes-defi.gitbook.io/plutus/ \n <:IRIS:904079866079608853> Iris Docs : https://hermes-defi.gitbook.io/hermes-finance/tokenomics-1/token \n <:wiki:969597819524636753> Wiki : https://wiki.hermesdefi.io/ \n <:github:969597819432341594> GitHub : https://github.com/Hermes-defi \n <:discord:969597819528814592> Discord : https://discord.gg/7CunQj4kbn \n <:twitter:969597819398811648> Twitter : https://twitter.com/hermesdefi \n <:medium:969597819579158569> Medium : https://blog.hermesdefi.io \n <:reddit:969597819457523823> Reddit : https://www.reddit.com/r/HermesDefi/ \n <:youtube:969597819637870652> Youtube : https://www.youtube.com/channel/UCnLWipB915XYPHMmMZcsnag  ",color=0x9208ea)    
    await ctx.send(embed=embed)

@client.command()
async def testnet(ctx):

  embed = discord.Embed(title="HermesDefi testnet Link",url="https://hermes-v3.vercel.app",color=0x97ffff)
  await ctx.send(embed=embed)

client.run(settings.TOKEN)      
