import random
from config_preset import c_attriw, c_bal_skill, c_jack_skill, c_spec_skill
from config_preset import skill_distro_list, attribute_base_pips, phys_skills_list, soc_skills_list, men_skills_list 

class WtA_stats:
        global ranpos, skillAtrri_dict, skills_pips, skill_distro

        ranpos = int(random.uniform(0,2))
        #random position within skills lists will be called both in skill specialization and skill distro functions
        skillAtrri_dict = {}

        if  c_bal_skill is True: 
            skill_distro = skill_distro_list [0][0]
            skill_pips = skill_distro_list [0][1]
        elif c_jack_skill is True:
            skill_distro = skill_distro_list [1][0]
            skill_pips = skill_distro_list [1][1]
        elif c_spec_skill is True:
            skill_distro = skill_distro_list[2][0]
            skill_pips = skill_distro_list[2][1]
        else:
            skill_distro = skill_distro_list[ranpos][0]
            skill_pips = skill_distro_list[ranpos][1]

        #@param:    string variable of weighted distribution type: Physical, Social, Mental, or None
        #@return:   dictionary of attribute items with max will and health keys calculated
        def attribute_generator(c_attriw =''):
            weighted_pip = attribute_base_pips [:3]
            attribute_pip = attribute_base_pips [3:]
            random.shuffle(weighted_pip)
            random.shuffle(attribute_pip)

            match c_attriw:
                #for physical weighted distribution
                case 'p':
                    strg    = weighted_pip[0]
                    dex     = weighted_pip[1]
                    stam    = weighted_pip[2]
                    char    = attribute_pip[0]
                    man     = attribute_pip[1]
                    comp    = attribute_pip[2]
                    intel   = attribute_pip[3]
                    wit     = attribute_pip[4]
                    resolve = attribute_pip[5]
                #for social weighted distribution
                case 's':
                    strg    = attribute_pip[0]
                    dex     = attribute_pip[1]
                    stam    = attribute_pip[2]
                    char    = weighted_pip[0]
                    man     = weighted_pip[1]
                    comp    = weighted_pip[2]
                    intel   = attribute_pip[3]
                    wit     = attribute_pip[4]
                    resolve = attribute_pip[5]
                #for mental weighted distribution
                case 'm':
                    strg    = attribute_pip[0]
                    dex     = attribute_pip[1]
                    stam    = attribute_pip[2]
                    char    = attribute_pip[3]
                    man     = attribute_pip[4]
                    comp    = attribute_pip[5]
                    intel   = weighted_pip[0]
                    wit     = weighted_pip[1]
                    resolve = weighted_pip[2]
                case _:
                    random.shuffle(attribute_base_pips)
                    strg    = attribute_base_pips [0]
                    dex     = attribute_base_pips [1]
                    stam    = attribute_base_pips [2]
                    char    = attribute_base_pips [3]
                    man     = attribute_base_pips [4]
                    comp    = attribute_base_pips [5]
                    intel   = attribute_base_pips [6]
                    wit     = attribute_base_pips [7]
                    resolve = attribute_base_pips [8]

            max_health = 3+stam
            max_will   = comp+resolve

            skillAtrri_dict.update({"Health":max_health})
            skillAtrri_dict.update({"Will":max_will,})
            skillAtrri_dict.update({"Strength (P)":strg})
            skillAtrri_dict.update({"Dexterity (P)":dex})
            skillAtrri_dict.update({"Stamina (P)":stam})
            skillAtrri_dict.update({"Charisma (S)":char})
            skillAtrri_dict.update({"Manipulation (S)":man})
            skillAtrri_dict.update({"Composure (S)":comp})
            skillAtrri_dict.update({"Intelligence (M)":intel})
            skillAtrri_dict.update({"Wits (M)":wit})
            skillAtrri_dict.update({"Reslove (M)":resolve})
            return skillAtrri_dict

        #@Param:    skill weighted preference: Physical, Social, Mental or random defined in config_preset.py
        #@Return:   updated Skills and Attributes dict
        def specialization_selector(pips = skill_pips):
           highest_pip = pips[0]

           match c_attriw:
                case 'm':
                    area = men_skills_list[random.randrange(0,len(men_skills_list)-1)]
                    subjs = area[1]
                    field = area[0]
                    expertise = subjs[random.randrange(0,len(subjs)-1,)]
                    skillAtrri_dict.update({'spec_skill':field})
                    skillAtrri_dict.update({'specialization':expertise})
                    skillAtrri_dict.update({'spec_skill_pip':highest_pip})
                case 'p':
                    area = phys_skills_list[random.randrange(0,len(phys_skills_list)-1)]
                    subjs = area[1]
                    field = area[0]
                    expertise = subjs[random.randrange(0,len(subjs)-1,)]
                    skillAtrri_dict.update({'spec_skill':field})
                    skillAtrri_dict.update({'specialization':expertise})
                    skillAtrri_dict.update({'spec_skill_pip':highest_pip})
                case 's':
                    area = soc_skills_list[random.randrange(0,len(soc_skills_list)-1)]
                    subjs = area[1]
                    field = area[0]
                    expertise = subjs[random.randrange(0,len(subjs)-1,)]
                    skillAtrri_dict.update({'spec_skill':field})
                    skillAtrri_dict.update({'specialization':expertise})
                    skillAtrri_dict.update({'spec_skill_pip':highest_pip})
                case __:
                    if ranpos == 0:
                        area = men_skills_list[random.randrange(0,len(men_skills_list)-1)]
                        subjs = area[1]
                        field = area[0]
                        expertise = subjs[random.randrange(0,len(subjs)-1,)]
                    elif ranpos == 1:
                        area = phys_skills_list[random.randrange(0,len(phys_skills_list)-1)]
                        subjs = area[1]
                        field = area[0]
                        expertise = subjs[random.randrange(0,len(subjs)-1,)]
                    else:
                        area = soc_skills_list[random.randrange(0,len(soc_skills_list)-1)]
                        subjs = area[1]
                        field = area[0]
                        expertise = subjs[random.randrange(0,len(subjs)-1,)]

           skillAtrri_dict.update({'spec_skill':field})
           skillAtrri_dict.update({'specialization':expertise})
           skillAtrri_dict.update({'spec_skill_pip':highest_pip})
           return skillAtrri_dict
        
        #@param: str skill_distro, list skill_pips
        #@param: updated skillAttri_dict with keys for populated skills
        def skills(pips = skill_pips[1:]):
            all_skills =[]
            random.shuffle(pips[0:])

            for list in phys_skills_list:
                all_skills.append(list[0])
                continue
            for list in soc_skills_list:
                all_skills.append(list[0])
                continue
            for list in men_skills_list:
                all_skills.append(list[0])
                continue

            for skill in all_skills:
                if skill == skillAtrri_dict.get('spec_skill'):
                    all_skills.remove(skill)
                    break
                else:
                    continue
            random.shuffle(all_skills)

            while len(pips) != 0:
                pip = pips[0]
                del pips[0]
                skill = all_skills[0]
                skillAtrri_dict.update({str(skill):pip})
                all_skills.remove(skill)
                random.shuffle(pips)
            return skillAtrri_dict

        #attribute_generator(c_attriw)
        #specialization_selector(skill_pips)
        #Sskills(skill_pips)