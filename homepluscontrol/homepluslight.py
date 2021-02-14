from .homeplusinteractivemodule import HomePlusInteractiveModule


class HomePlusLight(HomePlusInteractiveModule):
    """Class that represents a Home+ Light Module.
    
    This class extends the HomePlusInteractiveModule base class.
    """

    MODULE_BASE_URL='https://api.developer.legrand.com/hc/api/v1.0/light/lighting/addressLocation/plants/'
    """ API endpoint for the Home+ Light status """

    def __init__(self, plant, id, name, hw_type, device, fw='', type='', reachable = False):
        """ HomePlusLight Constructor 
        
        Args:
            plant (HomePlusPlant): Plant that holds this module
            id (str): Unique identifier of the module
            name (str): Name of the module
            hw_type (str): Hardware type(?) of the module (NLP, NLT, NLF)
            device (str): Type of the device (plug, light, remote)
            fw (str, optional): Firware(?) of the module. Defaults to an empty string.
            type (str, optional): Additional type information of the module. Defaults to an empty string.
            reachable (bool, optional): True if the module is reachable and False if it is not. Defaults to False.
        """
        super().__init__(plant, id, name, hw_type, device, fw, type, reachable)
        self.status = ''
        self.build_status_url(HomePlusLight.MODULE_BASE_URL)

    def __str__(self):
        """ Return the string representing this module """
        return f'Home+ Light: device->{self.device}, name->{self.name}, id->{self.id}, reachable->{self.reachable}, status->{self.status}'

