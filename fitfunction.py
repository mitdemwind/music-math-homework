import numpy as np
from population import Individual
from constants import *
from utils import *

# TODO
class FitFunction():
    def __init__(self):
        pass

    def __call__(self, music: Individual):
        # TODO
        return self._average_pitch_of_first_note(music)

    def _average_pitch_of_first_note(self, music: Individual) -> float:
        """
        Calculate the average pitch of the first note in the first measure.
        """
        first_measure = music.melody[0]
        first_note_pitch = first_measure[0]
        return np.mean(first_note_pitch)
    # need some helper functions

    @staticmethod
    def get_duration_series(music: Individual) -> np.ndarray:
        """ Returns the duration of each note in the music """
        dur_series = []
        current_dur=0
        for note in music.melody.ravel():
            if note not in EXTEND:
                dur_series.append(current_dur)
                current_dur = 1
            else:
                current_dur += 1
        dur_series.append(current_dur)

        return np.array(dur_series)
    

    
    #used to evaluate the complication of beats
    def get_duration_variance(self,music:Individual) -> float:
        return np.var(self.get_duration_series(music))

    def numbers_of_F_B_long_notes(self,music:Individual) -> int:
        """returns the number of F and B notes"""
        cnt=0
        duration_list=self.get_duration_series(music)
        pitch_list=self.get_pitch_series(music)
        for i in range(duration_list.size):
            if duration_list[i]>2 and to_pitchclass(pitch_list[i])[0] in [3,6]:
                cnt+=1
        return cnt

    def ratio_of_sharp_changes(self,music:Individual) -> float:
        """return the ratio of sharp-pitch changes between two notes"""
        pitch_list=self.get_pitch_series(music)
        cnt=0
        for i in range(pitch_list.size-1):
            if distance(pitch_list[i],pitch_list[i+1]>7):
                cnt+=1
        return cnt/pitch_list.size

    @staticmethod
    def get_pitch_series(music:Individual) -> np.ndarray:
        """ Returns the pitch number of each note """
        pitchlist=music.melody.ravel()
        mask = (pitchlist != -1)
        return pitchlist[mask]

    def reference_mean_total(self,music:Individual,musicr:Individual) -> float:
        """返回整体音高接近度"""
        pitchlist=self.get_pitch_series(music)
        pitchlistr=self.get_pitch_series(musicr)
        return abs(np.mean(pitchlist)-np.mean(pitchlistr))
    
    def reference_var_total(self,music:Individual,musicr:Individual) -> float:
        """返回整体起伏度"""
        pitchlist=self.get_pitch_series(music)
        pitchlistr=self.get_pitch_series(musicr)
        return abs(np.var(pitchlist)-np.var(pitchlistr))
    
    @staticmethod
    def only_pitch(music:Individual)->np.ndarray:
        """只考虑音高,将extend全部转为相应的音高值"""
        pitchlist=[]
        melodyflat=music.melody.ravel()
        for i in range(melodyflat.size):
            if i != EXTEND[0]:
                pitchlist.append(melodyflat[i])
            else:
                pitchlist.append(melodyflat[i-1])
        return np.array(pitchlist)
    
    def reference_detail(self,music:Individual,musicr:Individual) -> float:
        """返回细节上的接近度"""
        pitchlist=self.only_pitch(music)
        pitchlistr=self.only_pitch(musicr)
        return np.sum(abs(pitchlist-pitchlistr))
        
    def final_evaluate(self,music:Individual) ->float :
        return 50*(1-self.ratio_of_sharp_changes(music))-1*self.numbers_of_F_B_long_notes(music)+15*self.get_duration_variance(music)
        
    if __name__ == '__main__':
        a = Individual(np.array([[4,-1,-1,2,-1,3,-1,0], [2,-1,3,4,-1,-1,-1, 5], [2,3,5,-1,4,-1,-1, 2]]))
        b = Individual(np.array([[4,4,4,2,2,3,3,0], [2,2,3,4,4,4,4, 5], [2,3,5,5,4,4,4, 2]]))
        from fitfunction import FitFunction
        m=FitFunction()
        print(m.final_evaluate(a))
        print(m.final_evaluate(b))
