import attri_skill_gen
import charname_extractor

character = {}
charstats = attri_skill_gen.WtA_stats
nameslist = charname_extractor.extract_names()
name = nameslist[0]
character.update({'CharName':name})
character.update(charstats.attribute_generator())
character.update(charstats.specialization_selector())
character.update(charstats.skills())

print(character)