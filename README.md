# Wikipedia 📖 

  ## Search 👀 

  Searches for a particular word on wikipedia 
  
  >> print(search("wikipedia"))

  >> "Wikipedia is a free-content online encyclopedia written and maintained by a community of volunteers, collectively known as Wikipedians, through open collaboration and using a wiki-based editing system called           MediaWiki. Wikipedia is the largest and most-read reference work in history, and has consistently been one of the 10 most popular websites. Founded by Jimmy Wales and Larry Sanger on January 15, 2001, it is            hosted by the Wikimedia Foundation, an American nonprofit organization."

  ## Alike Words search 🔍 
  
  As there is no information about "Pink eye virus" but it is also called Conjuctivitis. So instead it search for Alike word

  >> print(search("pink eye virus"))
  
  >> Showing results of Conjunctivitis instead: 
  Conjunctivitis, also known as pink eye, is inflammation of the outermost layer of the white part of the eye and the inner surface of the eyelid. It makes the eye appear pink or reddish. Pain, burning, scratchiness,    or itchiness may occur. The affected eye may have increased tears or be "stuck shut" in the morning. Swelling of the white part of the eye may also occur. Itching is more common in cases due to allergies.              Conjunctivitis can affect one or both eyes.

  ## Suggestions 🤓

  Gives suggestions in array for words if exact word not found

  >> print(search("UMT"))
  
  >> ['Universal Mobile Telecommunications System', 'Metropolitan University of Tirana', "Moroccan Workers' Union (French: Union Marocaine du Travail)", 'Universal Military Training', 'Military Selective Service Act',   'UMT AG (United Mobility Technology AG) in Munich', 'University of Management and Technology', 'University of Management and Technology', 'Universiti Malaysia Terengganu (formerly known as KUSTEM)']

  ## No result 📕 

  Gives a answer when nothing found
  Let's give a random query

  >> print(search("abccdedhnesvi"))

  >> Unable to find information on 'abccdedhnesvi'. Recheck spellings

  That is for now :)

  
