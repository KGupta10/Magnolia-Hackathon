import PySimpleGUI as sg
import os

print(os.listdir())

recs = {
    'Fantasy': ["Shadow and Bone by Leigh Bardugo", 
                "The original fantasy saga from #1 New York Times bestselling author\nLeigh Bardugo, the Shadow and Bone Trilogy is the story of Alina \nStarkov, a soldier in the kingdom of Ravka who discovers she possesses \nmagical abilities. Training with the Grisha, her country's magical \nmilitary elite, Alina falls under the spell of their notorious leader,\nthe Darkling. He believes she is the only one with the power to \ndefeat the forces threatening the kingdom--forces that will test \nold alliances and challenge the very limits of magic, one that will\nforge a leader from a frightened girl.",
                "MagnoliaHacks\\images\\shadowAndBone.png"],
    'Sci-Fi': ["Arc of a Scythe by Neal Shusterman",
                "A world with no hunger, no disease, no war, no misery. Humanity has \nconquered all those things, and has even conquered death. Now scythes\nare the only ones who can end life—and they are commanded to do so, \nin order to keep the size of the population under control. Citra and \nRowan are chosen to apprentice to a scythe—a role that neither wants. \nThese teens must master the “art” of taking life, knowing that \nthe consequence of failure could mean losing their own.",
                "MagnoliaHacks\\images\\scythe.png"],
    'Realistic Fiction': ["The Fault in our Stars by John Green",
                            "Despite the tumor-shrinking medical miracle that has bought her a \nfew years, Hazel has never been anything but terminal, her final \nchapter inscribed upon diagnosis. But when a gorgeous plot twist \nnamed Augustus Waters suddenly appears at Cancer Kid Support Group,\nHazel's story is about to be completely rewritten.",
                            "MagnoliaHacks\\images\\faultInStars.png"],
    'Non-Fiction': ["The Invisible Kingdom by Meghan O'Rourke",
                    "A silent epidemic of chronic illnesses afflicts tens of millions of\nAmericans: these are diseases that are poorly understood, frequently\nmarginalized, and can go undiagnosed and unrecognized altogether.\nRenowned writer Meghan O’Rourke delivers a revelatory investigation\ninto this elusive category of “invisible” illness that encompasses\nautoimmune diseases, post-treatment Lyme disease syndrome, and now\nlong COVID, synthesizing the personal and the universal to help all\nof us through this new frontier.",
                    "MagnoliaHacks\\images\\invisKing.png"],
    'Historical Fiction': ["All the Light We Cannot See by Anthony Doerr",
                            "Marie-Laure lives in Paris near the Museum of Natural History, where\nher father works. When she is twelve, the Nazis occupy Paris and \nfather and daughter flee to the walled citadel of Saint-Malo, where\nMarie-Laure’s reclusive great uncle lives in a tall house by the sea.\nWith them they carry what might be the museum’s most valuable and\ndangerous jewel. In a mining town in Germany, Werner Pfennig, an \norphan, grows up with his younger sister, enchanted by a crude radio\nthey find that brings them news and stories from places they have\nnever seen or imagined. Werner becomes an expert at building and\nfixing these crucial new instruments and is enlisted to use his talent to\ntrack down the resistance. Deftly interweaving the lives of Marie-Laure\nand Werner, Doerr illuminates the ways, against all odds, people try to\nbe good to one another.",
                            "MagnoliaHacks\\images\\lightWeCantSee.png"],
    'Sports': ["She Drives Me Crazy by Kelly Quindlen",
                "Scottie is devastated when her girlfriend Tally breaks up with her\nand transfers to a “better” school the next town over. Now, Scottie\nand Tally are rivals on the basketball court, and it’s messing with\nher head. When a game goes poorly for Scottie, she accidentally gets\nin a fender bender with Irene Abraham, her school’s chilly cheerleading\ncaptain. Forced to carpool until Irene’s car is repaired, Scottie\nand Irene hatch up a fake dating scheme to make Tally jealous…but\nit backfires big time when both of them catch feelings! I loved how\nthis book talks about the nuances of unhealthy vs. healthy relationships,\nand how Quindlen explores Irene’s struggles to be recognized as an\nathlete in her chosen sport.",
                "MagnoliaHacks\\images\\drivesMeCrazy.png"],
    'Science':  ["Slay by Brittney Morris",
                "At school, Kiera Johnson is an honor roll student, math tutor, and\none of the only Black kids in her classes. But in the world she's\ncreated for herself, she is one of hundreds of thousands of Black gamers\ndueling in the online role-playing card game, Slay. Kiera is the game\ndeveloper, but no one in her \"real life\" knows about the project, and\nher identity is a secret online. When Slay is mentioned in relation\nto the murder of a Kansas City teen, Kiera is distraught.\nNews of the game and its Black-players-only rule reach media outlets,\nand Kiera's safe haven becomes a point of national discussion. When an anonymous\ntroll enters the game and threatens to sue over discrimination,\nKiera is determined to protect herself, her game, and her Blackness\nin a world that doesn't understand.",
                "MagnoliaHacks\\images\\slay.png"],
    'Music': ["Just Kids by Patti Smith",
                "It was the summer Coltrane died, the summer of love and riots, and\nthe summer when a chance encounter in Brooklyn led two young people\non a path of art, devotion, and initiation. Patti Smith would evolve as\na poet and performer, and Robert Mapplethorpe would direct his highly\nprovocative style toward photography. Bound in innocence and enthusiasm,\nthey traversed the city from Coney Island to Forty-Second Street,\nand eventually to the celebrated round table of Max’s Kansas\nCity, where the Andy Warhol contingent held court. In 1969, the pair\nset up camp at the Hotel Chelsea and soon entered a community of the famous and\ninfamous, the influential artists of the day and the colorful\nfringe. It was a time of heightened awareness, when the worlds of poetry,\nrock and roll, art, and sexual politics were colliding and exploding.\nIn this milieu, two kids made a pact to take care of each other.\nScrappy, romantic, committed to create, and fueled by their mutual\ndreams and drives, they would prod and provide for one another during the hungry years.",
                "MagnoliaHacks\\images\\justKids.png"]
}

# ----------- Create the 3 layouts this Window will display -----------
home_page = [[sg.Text('Welcome to the Reading Recommender!')], 
             [sg.Button('Get Started')],
             [sg.Button('Other Resources')],
             [sg.Button('About This Program')]]

rec_page = [[sg.Text('Do you like reading?'), sg.RButton('Yes'), sg.RButton('No')], 
            [sg.Column([[sg.Text('What is your favorite genre?'), sg.Combo(['Fantasy', 'Sci-Fi', 'Realistic Fiction', 'Non-Fiction', 'Historical Fiction'], key='-reading_menu-', readonly=True, enable_events=True)]], key='-reading_options-', visible=False),
             sg.Column([[sg.Text('What is your favorite hobby?'), sg.Combo(['Sports', 'Science', 'Music'], key='-hobbies_menu-', readonly=True, enable_events=True)]], key='-hobbies_options-', visible=False)],
             [sg.Button('View my recomendation!', key='-rec_button-', visible=False)],
             [sg.Column([[sg.Text(recs[genre][0])], [sg.Text(recs[genre][1])], [sg.Image(recs[genre][2])]], visible=False, key=f'-{genre}-') for genre in recs.keys()]]

resources_page = [[sg.Text('Other Resources for Book Recommendations')],
                  [sg.Text('Goodreads')],
                  [sg.Text('Bookstagram')],
                  [sg.Text('Booktok')],
                  [sg.Text('Booktube')]]

about_page = [[sg.Text('About This Program')],
              [sg.Text("There is currently a gender gap in reading/writing books. Many people,\nespecially men and boys, don't read books by women or with female\nprotagonists. This instills harmful gender stereotypes from an early\nage and is detrimental to society. \n\nOne cause of this is that books are generally marketed with stereotypes\nin mind. Superheroes and horror are directed toward males and princesses\nand romance are directed toward females. Instead of focusing on gender,\nbooks should be targeted based on interests/hobbies. That's what\nthis program aims to do. It recommends books written by women or\nwith femaleprotagonists to the user based on what they like to read/do.\nIt'sthe first step in closing the gender gap in readingand together,\nwe can solve this prominent issue!")]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(home_page, key='-home_page-'), sg.Column(rec_page, key='-rec_page-', visible=False), sg.Column(resources_page, key='-resources_page-', visible=False), sg.Column(about_page, key='-about_page-', visible=False)], 
          [sg.Button('Home')]]

window = sg.Window('Reading Recommender', layout)

category = ''

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Home':
        window['-home_page-'].update(visible=True)
        window['-rec_page-'].update(visible=False)
        window['-resources_page-'].update(visible=False)
        window['-about_page-'].update(visible=False)
    elif event == 'Get Started':
        window['-home_page-'].update(visible=False)
        window['-rec_page-'].update(visible=True)
        window['-resources_page-'].update(visible=False)
        window['-about_page-'].update(visible=False)
    elif event == 'Other Resources':
        window['-home_page-'].update(visible=False)
        window['-rec_page-'].update(visible=False)
        window['-resources_page-'].update(visible=True)
        window['-about_page-'].update(visible=False)
    elif event == 'About This Program':
        window['-home_page-'].update(visible=False)
        window['-rec_page-'].update(visible=False)
        window['-resources_page-'].update(visible=False)
        window['-about_page-'].update(visible=True)
    elif event == 'Yes':
        window['-reading_options-'].update(visible=True)
        window['-hobbies_options-'].update(visible=False)
        window['-rec_button-'].update(visible=False)
        for key in recs.keys():
            window[f'-{key}-'].update(visible=False)
    elif event == 'No':
        window['-reading_options-'].update(visible=False)
        window['-hobbies_options-'].update(visible=True)
        window['-rec_button-'].update(visible=False)
        for key in recs.keys():
            window[f'-{key}-'].update(visible=False)
    elif event == '-reading_menu-' or event == '-hobbies_menu-':
        window['-rec_button-'].update(visible=True)
        category = values[event]
    elif event == '-rec_button-':
        for key in recs.keys():
            window[f'-{key}-'].update(visible=False)
        window[f'-{category}-'].update(visible=True)

window.close()