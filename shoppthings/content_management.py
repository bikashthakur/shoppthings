'''------------------------- FORMAT : ['title', 'img-source', 'price']------------------------------------------------------------------'''

def Content():
	items = { "Mobiles" : { "mob01" :	['Samsung Companion','../static/_images/mobiles/samsung-companion.jpg','6,999'],
							"mob02" :	['Apple Watch iPhone 6s 32GB','../static/_images/mobiles/apple-watch-iphone-6s.jpg','39,999'],
							"mob03" :	['HTC-Titan','../static/_images/mobiles/htc-titan.jpg','21,998'],
							"mob04" :	['Lenovo-A6000','../static/_images/mobiles/lenovo-a-6000.jpg','9,898'],
							"mob05" :	['Nokia-Lumia 820','../static/_images/mobiles/lumia-820.jpg','12,449'],
							"mob06" :	['Xiaomi Redmi 3 Fashion Gold','../static/_images/mobiles/redmi-3-gold.jpg','8,449'],
							"mob07" :	['Samsung Curve','../static/_images/mobiles/samsung-curve.jpg','12,998'],
							"mob08" :	['Redmi Prime Black (Black 16GB)','../static/_images/mobiles/redmi-prime.jpg','13,999'],
							"mob09" :	['Xperia C5 Ultra White','../static/_images/mobiles/xperia-c5-ultra-white.png','15,999'],
							"mob10" :	['Coolpad Note 3 Plus','../static/_images/mobiles/coolpad-note-3-plus.jpg','12,449'],
							"mob11" :	['Nokia-Lumia 925','../static/_images/mobiles/lumia-925.jpg','10,449'],
							"mob12" :	['Samsung S Bike Mode','../static/_images/mobiles/samsung-bike-mode.jpg','9,999'] },

				"MensClothing" : { "mens01" :	["Alan Jones Printed Men's Round Neck Blue, Grey T-Shirt",'../static/_images/clothings/alan-jones00.jpeg','1798','58','749'],
									"mens02" :	["Roadster Solid Men's Polo Neck Black T-Shirt (Pack of 2)",'../static/_images/clothings/roadster03.jpeg','949','20','759'],
									"mens03" :	["Alan Jones Solid Men's V-Neck Silver, Black T-Shirt",'../static/_images/clothings/alan-jones04.jpeg','1398','64','499'],
									"mens04" :	["Roadster Solid Men's Round Neck Grey T-Shirt (Pack of 2)",'../static/_images/clothings/roadster06.jpeg','899','20','719'],
									"mens05" :	["John Player's Red Checked Regular Fit Casual Shirt ",'../static/_images/clothings/redcheckedshirt.jpg','1299','23','999'],
									"mens06" :	["Maniac Printed Men's Round Neck Multicolor T-Shirt",'../static/_images/clothings/maniac00.jpeg','1797','69','549'],
									"mens07" :	["Duke Stardust Striped Men's Polo Neck Grey, Black T-Shi...",'../static/_images/clothings/duke00.jpeg','875','15','743'],
									"mens08" :	["Fort Collins Solid Men's Grey, Green T-Shirt (Pack of 2)",'../static/_images/clothings/fort00.jpeg','499','17','411'],
									"mens09" :	["Rodid Solid Men's V-neck Black, Grey T-Shirt (Pack of 2)",'../static/_images/clothings/rodid01.jpeg','2100','69','649'],
									"mens10" :	["Alan Jones Solid Men's Henley Black, Grey T-Shirt (Pack of 2)",'../static/_images/clothings/alan-jones02.jpeg','1798','98','649'],
									"mens11" :	["Alan Jones Printed Men's Hooded Black, Grey T-Shirt (Pack of 2)",'../static/_images/clothings/alan-jones03.jpeg','1998','60','799'],
									"mens12" :	["Dazzio Black Plain Men's Party Wear Shirt (Pack of 2)",'../static/_images/clothings/dazzio00.jpg','1797','69','549'],
									"mens13" :	["Rodid Solid Men's Henley Grey, Grey T-Shirt (Pack of 2)",'../static/_images/clothings/rodid00.jpeg','2198','70','649'],
									"mens14" :	["Polo Green Men's Solid T-Shirt.",'../static/_images/clothings/polotshirt.jpg','1299','23','999'],
									"mens15" :	["Green Striped Traditional Kurta ",'../static/_images/clothings/green-striped-kurta.jpg','1998','60','799'],
									"mens16" :	["Maroon Graphic Printed Men's T-Shirt",'../static/_images/clothings/maroon-graphic-print-men-t-shirt.jpg','1299','23','999'] } }
	return items


'''--------------- FORMAT : ['title', 'img-source', 'old-price', 'off%','price']---------------------------------------------------------------------------------------------------'''

def homeContent():
	homeItems = { "Mobiles" : { "mobhome01" : ['Moto G Plus, 4th Gen...', '../static/_images/mobiles/motog-plus.jpg', '15,999', '25', '11,999'],
								"mobhome02" : ['OnePlus 3 64GB','../static/_images/mobiles/one-plus-3.jpg', '27,999','25','20,999'],
								"mobhome03" : ['iPhone 7s 32GB Gold','../static/_images/mobiles/iphone7.jpg', '59,999','10','54,999'],
								"mobhome04" : ['Lenovo Vibe 5 Note 16GB','../static/_images/mobiles/lenovo-vibe.jpg', '9,999','25','7,449']},
								
					"MensClothing" : { "menshome01" : ["Rodid Men's Solid Casual T-Shirt (Pack of 2)",'../static/_images/clothings/roadster01.jpeg','1,199','25','7,999' ],
										"menshome02" : ["Rodid Men's Solid Casual Shirt (Pack of 2)",'../static/_images/clothings/rodid02.jpeg', '1599','50','7,999'],
										"menshome03" : ["John Player's Solid Men's V-neck T-Shirt...",'../static/_images/clothings/roadster00.jpeg', '1,199','50','5,999'],
										"menshome04" : ["Roadster Solid Men's V-neck T-Shirt (Pack of 2)",'../static/_images/clothings/roadster03.jpeg', '1,999','25','1,499']},
									
					"Shoes"	: { "shoeshome01" : ['Puma Sporty Light Shoes','../static/_images/shoes/shoes5.jpg','3,999','25','2,999'],
								"shoeshome02" : ['Reebok Sport Shoes','../static/_images/shoes/shoes3.jpg','3,599','25','2,699'],
								"shoeshome03" : ['Highlander"s Fashion Shoes','../static/_images/shoes/shoes6.jpg', '2,999','33','1,999'],
								"shoeshome04" : ['Leather Shoes','../static/_images/shoes/shoes7.jpg',' 3,499','50','1,999']}}
	return homeItems