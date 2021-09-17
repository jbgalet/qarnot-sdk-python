from typing import Dict
import abc

# ********************************************************
# *******************  Filtering  ************************
# ********************************************************


class AbstractFiltering(metaclass=abc.ABCMeta):
    """
    Abstract base class for resources filtering, allowing to select only a subset of a resources bucket as task resources.
    """
    @abc.abstractmethod
    def to_json(self):
        """Get a dict ready to be json packed.

        :raises NotImplementedError: this is an abstract method, it should be overridden in child classes
        """

    @classmethod
    @abc.abstractmethod
    def from_json(cls, json):
        """Static method called to create the class obj from a json object.

        :param json: the json elements of the class
        :type json: Dict
        :raises NotImplementedError: this is an abstaract method, override it in it's child classes.
        """


class BucketPrefixFiltering(AbstractFiltering):
    name: str = 'prefixFiltering'

    """
        Allows to filter a resources bucket by name prefix. Only bucket files starting with the given prefix will be used as task resources.
    """
    def __init__(self, prefix: str):
        self.prefix = prefix

    @classmethod
    def from_json(cls, json: Dict[str, str]):
        """Static method called to create the class obj from a json object.

        :param json: the json elements of the class
        :type json: Dict
        "bucket_or_bucket_name""
        """
        prefix = json.get("prefix")
        return BucketPrefixFiltering(prefix)

    def __repr__(self) -> str:
        return "Filtering: {}  prefix: {}".format(self.name, self.prefix)

    def to_json(self) -> object:
        """Get a dict ready to be json packed.
        :return: the json elements of the class.
        :rtype: Dict

        """
        return {
            "prefix": self.prefix
        }


class Filtering(object):
    """
        Groups the various object filters on an advanced resources bucket.
    """

    def __init__(self):
        self._filters = {}

    def __repr__(self) -> str:
        return "[" + ",".join(map(str, self._filters.values())) + "]"

    def append(self, filtering: AbstractFiltering):
        """Add a new filtering object

        :param filtering: a filtering object of the bucket
        :type filtering: FilteringObject
        """
        self._filters[filtering.name] = filtering

    @classmethod
    def from_json(cls, json) -> object:
        """Create the class sub objects of a Filtering from a json.

        :param json: the json elements of the class
        :type json: Dict
        """
        filtering = Filtering()
        for key in json:
            if BucketPrefixFiltering.name == key:
                filtering.append(BucketPrefixFiltering.from_json(json[key]))
        return filtering

    def to_json(self) -> object:
        """Get a dict ready to be json packed.
        """
        json = {}
        for key in self._filters:
            json[key] = self._filters[key].to_json()
        return json

# ********************************************************
# *************  ResourcesTransformation  ****************
# ********************************************************


class AbstractResourcesTransformation(metaclass=abc.ABCMeta):
    """
    Abstract base class for resources transformation, allowing to transform bucket objects before they are presented to the task as resources.
    """

    @abc.abstractmethod
    def to_json(self):
        """Get a dict ready to be json packed.
        """

    @classmethod
    @abc.abstractmethod
    def from_json(cls, json):
        """Static method called to create the class obj from a json object.

        :param json: the json elements of the class
        :type json: Dict
        """


class PrefixResourcesTransformation(AbstractResourcesTransformation):
    """
        Allows to remove a prefix from bucket files before they are presented to the task. During execution, the task will see files with paths stripped of the given prefix in its working directory.
    """
    name: str = 'stripPrefix'

    def __init__(self, prefix: str):
        """The PrefixResourcesTransformation constructor

        :param prefix: the prefix path of the resource bucket to be removed.
        :type prefix: str
        """
        self.prefix = prefix

    def __repr__(self) -> str:
        return "ResourcesTransformation: {}  prefix: {}".format(self.name, self.prefix)

    @classmethod
    def from_json(cls, json):
        """Create a new instance of the class using the given json object.

        :param json: The Json object representation.
        :type json: Dict
        :return: The PrefixResourcesTransformation new object
        :rtype: PrefixResourcesTransformation
        """
        return PrefixResourcesTransformation(json["prefix"])

    def to_json(self) -> object:
        """Get a dict ready to be json packed.
        """
        return {
            "prefix": self.prefix
        }


class ResourcesTransformation(object):
    """
        Groups the various object transformation on an advanced resources bucket.
    """
    def __init__(self):
        self._resource_transformers = {}

    def append(self, resource: AbstractResourcesTransformation):
        """Add a new resource transformation object

        :param filtering: a filtering object of the bucket
        :type filtering: FilteringObject
        """
        self._resource_transformers[resource.name] = resource

    def __repr__(self) -> str:
        return "[" + ",".join(map(str, self._resource_transformers.values())) + "]"

    @classmethod
    def from_json(cls, json) -> object:
        """Create the class sub objects of a ResourcesTransformation from a json.

        :param json: the json elements of the class
        :type json: Dict
        """
        resource = ResourcesTransformation()
        for key in json.keys():
            if PrefixResourcesTransformation.name == key:
                resource.append(
                    PrefixResourcesTransformation.from_json(json[key]))
        return resource

    def to_json(self) -> object:
        """Get a dict ready to be json packed.
        """
        json = {}
        for key in self._resource_transformers.keys():
            json[key] = self._resource_transformers[key].to_json()
        return json
