import random

animal_name1 = ['Abominable', 'Agitated', 'Bane', 'Blight', 'Brood', 'Chaos', 'Cruel', 'Cursed', 'Damned', 'Decay', 'Dirty', 'Dust', 'Eternal', 'Fang', 'Fetid', 'Flail', 'Flame', 'Fog', 'Foul', 'Frost', 'Fungus', 'Gas', 'Ghoul', 'Greater', 'Grime', 'Groaning', 'Haunt', 'Herd', 'Howling', 'Infernal', 'Jelly', 'Lesser', 'Mantis', 'Mold', 'Murk', 'Noxious', 'Outlandish', 'Phase', 'Plague', 'Poison', 'Putrid', 'Radiant', 'Razor', 'Retch', 'Rot', 'Savage', 'Screeching', 'Shadow', 'Slime', 'Smog', 'Spore', 'Stealth', 'Stink', 'Tall', 'Terror', 'Toxic', 'Ugly', 'Vicious', 'Vortex', 'Warp', 'Wave', 'Web', 'Wisp']
animal_name2 = ['Assassin', 'Aura', 'Babbler', 'Beast', 'Behemoth', 'Blast', 'Blob', 'Brute', 'Charmer', 'Creeper', 'Critter', 'Enveloper', 'Fang', 'Fisher', 'Freak', 'Frill', 'Ghost', 'Grasper', 'Herder', 'Horror', 'Howler', 'Jelly', 'Lump', 'Lure', 'Mammoth', 'Maw', 'Mirage', 'Morph', 'Nightmare', 'Ooze', 'Orb', 'Pest', 'Ripper', 'Seeker', 'Sentinel', 'Snare', 'Spawn', 'Stinger', 'Strider', 'Strike', 'Swarm', 'Tangler', 'Wing']
armor_class = ['13', '14', '14', '15', '15', '15', '16', '17', '18']
hit_dice = ['1', '1', '1', '1', '1','1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '5', '6', '7', '8', '9', '10']
movement_rate = ['10', '15', '15', '15', '20']
number_attacks = ['1', '1', '1', '1', '1', '2', '2', '3']
first_attack = ['1 bite', '1 bite', '1 bite', '1 bite', '1 bite', '1 claw', '1 claw', '1 claw', '1 gore', '1 pincer', '1 kick', '1 tentacle', '1 beak']
second_attack = ['1 claw', '1 claw', '1 claw', '2 claws', '1 tentacle', '1 squeeze', '1 trample', '1 touch', '1 breath', '1 sting', '1 spit' ]
third_attack = ['+ poison', '+ poison', '+ poison', '+ poison', '+ poison', '+ paralysis', '+ paralysis', '+ paralysis', '+ convulsions', '+ convulsions', '+ hallucinations', '+ hallucinations', '+ blindness', '+ death']
roll_damage1 = ['1d3', '1d3', '1d4', '1d4', '1d4', '1d4', '1d4', '1d4', '1d6', '1d6', '1d6', '1d8', '1d10', '1d12']
roll_damage2 = ['1d3', '1d3', '1d4', '1d4', '1d4', '1d4', '1d4', '1d4', '1d6', '1d6', '1d6', '1d8', '1d10', '1d12']
beast_morale = ['7', '8', '9', '9', '9', '9', '9', '9', '10', '11', '12']
basic_animal = ['Amphibian, froggish or newtlike', 'Bird, winged and feathered', 'Fish, scaled and torpedo-bodied', 'Insect, beetle-like or fly-winged', 'Mammal, hairy and fanged', 'Reptile, lizardlike and long-bodied', 'Spider, many-legged and fat', 'Exotic, made of wholly alien elements']
body_plan = ['Humanoid', 'Quadruped', 'Many-legged', 'Bulbous', 'Amorphous']
limb_novelty = ['Wings', 'Many joints', 'Tentacles', 'Opposable thumbs', 'Retractable', 'Varying sizes']
skin_novelty = ['Hard shell', 'Exoskeleton', 'Odd texture', 'Molts regularly', 'Harmful to touch', 'Wet or slimy']
main_weapon = ['Teeth or mandibles', 'Claws', 'Poison', 'Harmful discharge', 'Pincers', 'Horns']
animal_size = ['Cat-sized', 'Wolf-sized', 'Calf-sized', 'Bull-sized', 'Hippo-sized', 'Elephant-sized']
option_predator = ['Hunts in kin-group packs', 'Favors ambush attacks', 'Cripples prey and waits for death', 'Pack supports alpha-beast attack', 'Lures or drives prey into danger', 'Hunts as a lone, powerful hunter', 'Only is predator at certain times', 'Breeds at tremendous rates']
option_prey = ['Moves in vigilant herds', 'Exists in small family groups', 'They all team up on a single foe', 'They go berserk when near death', 'They are violent in certain seasons', 'They are vicious if threatened', 'Symbiotic creature protects them', 'Breeds at tremendous rates']
option_scavenger = ['Never attacks unwounded prey', 'Uses other beasts as harriers', 'Always flees if significantly hurt', 'Poisons prey, waits for it to die', 'Disguises itself as its prey', 'Remarkably stealthy', 'Summons predators to weak prey', 'Steals prey from weaker predator']
harmful_discharge = ['Acidic spew doing its damage on a hit', 'Toxic spittle or cloud, use adjacent chart', 'Super-heated or super-chilled spew', 'Sonic drill or other disabling noise', 'Natural laser or plasma discharge', 'Nauseating stench or disabling chemical', 'Equipment-melting corrosive', 'Explosive pellets or chemical catalysts']
option_poison = ['Death', 'Paralysis', '1d4 dmg per onset interval', 'Convulsions', 'Blindness', 'Hallucinations']
option_onset = ['Instant', '1 round', '1d6 rounds', '1 minute', '1d6 minutes', '1 hour']
option_duration = ['1d6 rounds', '1 minute', '10 minutes', '1 hour', '1d6 hours', '1d6 days']

for i in range(100):
    print('Beast Type: {name1} {name2} \n AC: {ac} \n HD: {hd} \n #Attacks {atk}: {atk1}/{atk2}/{atk3} \n Damage: {d1}/{d2}/+special \n Movement Rate: {mv}m \n Morale: {ml} \n Skills: +{hd} \n Saves: (16-{hd})+ \n Basic Animal: {animal} \n Body Plan: {body} \n Limb Novelty: {limb} \n Skin Novelty: {skin} \n Main Weapon: {weapon} \n Size: {size} \n Predator: {predator} \n Prey: {prey} \n Scavenger: {scavenger} \n Harmful Discharge: {discharge} \n Poison: {poison} \n Onset: {onset} \n Duration: {duration} \n'.format(
        name1=random.choice(animal_name1),
        name2=random.choice(animal_name2),
        ac=random.choice(armor_class),
        hd=random.choice(hit_dice),
        mv=random.choice(movement_rate),
        atk=random.choice(number_attacks),
        atk1=random.choice(first_attack),
        atk2=random.choice(second_attack),
        atk3=random.choice(third_attack),
        d1=random.choice(roll_damage1),
        d2=random.choice(roll_damage2),
        ml=random.choice(beast_morale),
        animal=random.choice(basic_animal),
        body=random.choice(body_plan),
        limb=random.choice(limb_novelty),
        skin=random.choice(skin_novelty),
        weapon=random.choice(main_weapon),
        size=random.choice(animal_size),
        predator=random.choice(option_predator),
        prey=random.choice(option_prey),
        scavenger=random.choice(option_scavenger),
        discharge=random.choice(harmful_discharge),
        poison=random.choice(option_poison),
        onset=random.choice(option_onset),
        duration=random.choice(option_duration)))
