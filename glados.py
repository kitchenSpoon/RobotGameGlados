import rg
import random as r

class Robot:
    def act(self, game):
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game['robots'].iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

	if(r.randint(0,1)==1):
        	# move toward the center
        	return ['move', rg.toward(self.location, rg.CENTER_POINT)]		
	else:
		# move towards closest ally
		loc=r.choice(rg.locs_around(self.location, filter_out=('invalid', 'obstacle','spawn')))
		return ['move', rg.toward(self.location,loc)]
