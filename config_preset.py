import json
import random
class predfined_values:
        #read from config file for predefined parameters for character
    global c_name, c_auspice, c_patron, c_tribe, c_concept, c_attriw, c_jack_skill, c_spec_skill, c_bal_skill
    global phys_skills_list, soc_skills_list, men_skills_list, skill_distro_list, attribute_base_pips 
    def __init__ (config):
        config_file = open('config.json','r')
        config.self = json.load(config_file)
        c_name    = config['char_name']
        c_auspice = config['auspice']
        c_patron  = config['patron']
        c_tribe   = config['tribe']
        c_concept = config['concept']
        c_attriw  = config['attri_weight']
        c_bal_skill  =config['bal_skill_distr']
        c_jack_skill = config['jack_skill_distr']
        c_spec_skill = config['spec_skill_distr'] 
        return c_name,c_auspice,c_patron,c_tribe,c_concept,c_attriw,c_bal_skill,c_jack_skill,c_spec_skill



    skill_distro_list = [('balanced',[3,3,3,2,2,2,2,2,1,1,1,1,1,1,1]), #balanced
                        ('jack of all trades',[3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]),#jack of all trades
                        ('special',[4,3,3,3,2,2,2,1,1,1])] #'special'
    
    attribute_base_pips = [4,3,3,3,2,2,2,2,1]
    
    phys_skills_list = [('Athletics',('Acrobatics','Climbing','Endurance','Jumping','Parkour','Swimming','Throwing')),
                            ('Brawl',('Animals','Armed Humans','Bar Fights','Ceremonial Combat','Grappling','Unarmed Humans')),
                            ('Craft',('Carpentry','Caern Rites','Design','Painting','Sculpting','Sewing','Weaponsmithing')),
                            ('Firearms',('Crossbows', 'Gun Dealing', 'Gunsmithing','Handloading Ammunition', 'Quick Draw', 'Sniper', 'TrickShooting')),
                            ('Driving',('All-Terrain Vehicles','Construction Vehicles','Evasive Driving','Motorcycles','Street Racing','Stunts','Tailing','Trucks','Vintage Model Cars')),
                            ('Larceny',('Alarms','Forgery','Grand Theft Auto','House-Breaking','Lockpicking', 'Pickpocketing','Safecracking','Security Analysis')),
                            ('Melee',('Axes','Chains','Clubs','Foils','Disarming Blows','Garrotes','Improvised Weapons','Knives','Stakes','Swords')),
                            ('Stealth',('Ambushes','Crowds','Disguise','Hiding','Shadowing','Urban','Wilderness')),
                            ('Survival',('Desert','Hunting','Jungle','Tracking','Traps','Shelters','Urban','Woodlands'))]
    
                    
    soc_skills_list =   [('Animal Ken',('Attack Training', 'Cats', 'Dogs', 'Falconry','Horses', 'Pacification', 'Rats', 'Snakes', 'Wolves')),
                            ('Etiquette',('Celebrities', 'Corporate', 'Garou', 'One-Percen-ter', 'Spirits', 'Secret Society')),
                            ('Insight',('Discerning Lies','Empathy','Interrogation','Motives','Phobias','Spirits','Vices')),
                            ('Intimidation',('Animals','Armed Humans','Bar Fights','Ceremonial Combat','Grappling','Unarmed Humans')),
                            ('Leadership',('Command','Down But Not Out','Inspiration','Oratory','Team Dynamics','War Pack')),
                            ('Performance',('All-Terrain Vehicles','Construction Vehicles','Evasive Driving','Motorcycles','Street Racing','Stunts','Tailing','Trucks','Vintage Model Cars')),
                            ('Persuasion',('Bargaining','Fast Talk','Interrogation','Legal Argument','Negotiation','Nonstop Bullshit','Rhetoric')),
                            ('Streetwise',('Arms Dealing','Black Market','Bribery','Drugs','Fence Stolen Goods','Gangs',' Graffiti','Sex Trade','The Best Parties')),
                            ('Subterfuge',('Bluff','Corporate Double-Talk','Impeccable','Lies','Innocence','The Long Con','Seduction'))]
        
    men_skills_list =   [('Academics',('African Literature', 'Architecture', 'History of Art', 'History (specific Field or Period)', 
                                        'Migration Practices of Predatory Animals', 'Journalism','Philosophy','Research', 'Teaching', 'Theology')),
                            ('Awareness',('Ambushes', 'Camouflage', 'Concealed Objects','Hearing', 'Instincts', 'Smell', 'Sight', 'Traps', 'Wilderness')),
                            ('Finance',('Appraisal','Banking, Black Markets', 'Corporate Finance','Currency Manipulation',
                                    'Emerging Markets', 'Forensic Accounting','Meme Stock Speculation','Money Laundering')),
                            ('Investigation',('Criminology','Deduction','Forensics','Missing Persons','Murder','Racketeering','Traffic Analysis')),
                            ('Medicine',('First Aid','Hematology','Pathology','Pharmacy','Phlebotomy','Surgery','Trauma Care','Veterinary')),
                            ('Occult',('Alchemy','Faeries','Ghosts','Goetia','Grimoires','Metaphysics','Parapsychology','Spirits','Umbra')),
                            ('Politics',('City Government', 'Diplomacy', 'Media,National Politics', 'Pack Territories', 'State or Provincial Politics')),
                            ('Science',('Astronomy','Biology','Chemistry','Demolitions','Engineering','Genetics','Geology','Mathematics','Physics')),
                            ('Technology',('Artillery, Coding','Computer Construction,Data Mining','Energy Systems','Hacking','Networks','Phones','Surveillance Systems'))]
