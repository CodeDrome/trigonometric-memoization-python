import math


class TrigonometricMemoization(object):

    """
    Stores sines of 0 to 90 degrees in a list.
    These are used as the basis of calculating and
    returning sines, cosines and tangents of any angle.
    """

    def __init__(self):

        """
        Calculates sines of 0 to 90 degrees and appends them to a list.
        """

        self.memoized_sines = []

        degrees_in_radian = 180.0 / math.pi

        for d in range(0, 91):

            self.memoized_sines.append(math.sin(d / degrees_in_radian))

    def sine(self, degrees):

        """
        Calculates sine of any angle from values stored in list.
        """

        sine_negative = False

        # get an angle between -360 and 360 using modulus operator
        degrees_shifted = degrees % 360

        # move negative angles by 360 into the positive range
        if(degrees_shifted < 0):
            degrees_shifted += 360

        # if angle is in the 180-360 range shift it to the 0-180 range
        # and record that we need to negate the sine
        if(degrees_shifted > 180):
            degrees_shifted-= 180
            sine_negative = True

        # if degrees_shifted is 90-180 we need to "mirror" it into the 0-90 range
        if(degrees_shifted > 90 and degrees_shifted <= 180):
            degrees_shifted = 90 - (degrees_shifted - 90)

        # now get the sine from the memoized lookup table
        sine = self.memoized_sines[degrees_shifted]

        # negate if angle was 180-360
        if(sine_negative):
            sine*= -1

        return sine

    def cosine(self, degrees):

        """
        Cosine can easily be calculated from sine by shifting 90 degrees.
        """

        return self.sine(degrees + 90)

    def tangent(self, degrees):

        """
        Tangent is calculated using the sine and cosine from the other two methods.
        """

        try:

            sine = self.sine(degrees)
            cosine = self.cosine(degrees)

            return sine / cosine

        except:

            return math.nan
