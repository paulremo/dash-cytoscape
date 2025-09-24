# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal  # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class Cytoscape(Component):
    """A Cytoscape component.


    Keyword arguments:

    - id (string; optional):
        The ID used to identify this component in Dash callbacks.

    - autoRefreshLayout (boolean; default True):
        Whether the layout should be refreshed when elements are added or
        removed.

    - autolock (boolean; default False):
        Whether nodes should be locked (not draggable at all) by default
        (if True, overrides individual node state).

    - autoungrabify (boolean; default False):
        Whether nodes should be ungrabified (not grabbable by user) by
        default (if True, overrides individual node state).

    - autounselectify (boolean; default False):
        Whether nodes should be unselectified (immutable selection state)
        by  default (if True, overrides individual element state).

    - boxSelectionEnabled (boolean; default False):
        Whether box selection (i.e. drag a box overlay around, and release
        it  to select) is enabled. If enabled, the user must taphold to
        pan the graph.

    - className (string; optional):
        Sets the class name of the element (the value of an element's html
        class attribute).

    - clearOnUnhover (boolean; default False):
        If set to True, mouseoverNodeData and mouseoverEdgeData will be
        cleared on unhover.  If set to False, the value of
        mouseoverNodeData and mouseoverEdgeData will be the last  Node or
        Edge hovered over.

    - contextMenu (list of dicts; optional):
        Define a custom context menu. The behaviour of each menu item can
        be defined in 1 of 3 ways.  1. By passing a string to onClick that
        refers to one of the built-in Javascript functions.  2. By passing
        a string to onClickCustom that refers to one of the user-defined
        functions in a namespace.  3. By omitting both of these
        properties; this will update the contextMenuData property and
        trigger a Dash callback.

        `contextMenu` is a list of dicts with keys:

        - id (string; required):
            ID of the menu item in the context menu.

        - label (string; required):
            The label on the context menu item.

        - tooltipText (string; optional):
            The tooltip text when hovering on top of a context menu item.

        - availableOn (list; optional):
            A list containing either 'node', 'edge',and/or 'canvas'. This
            will determine where the context   menu item will show up.

        - onClick (string; optional):
            Specify which built-in JavaScript function to use as behaviour
            for the context  menu item. One of 'remove', 'add_node', or
            'add_edge'.

        - onClickCustom (string; optional):
            Specify which user-defined Javascript function to use in the
            dashCytoscapeFunctions  namespace as behaviour for the context
            menu item.

    - contextMenuData (dict; optional):
        Retrieve relevant data when a context menu item is clicked.
        Read-only.

        `contextMenuData` is a dict with keys:

        - menuItemId (string; optional):
            ID of the menu item in the context menu.

        - x (number; optional):
            x-position of the context click.

        - y (number; optional):
            y-position of the context click.

        - timeStamp (number; optional):
            Timestamp of context click.

        - elementId (string; optional):
            Element ID on context click if the context click was on an
            element.  If context click was on white space, this property
            is not returned.

        - edgeSource (string; optional):
            Node ID of the edge source if the clicked element is an edge,
            or else this property is not returned.

        - edgeTarget (string; optional):
            Node ID of the edge target if the clicked element is an edge,
            or else this property is not returned.

    - elements (list of dicts; optional):
        A list of dictionaries representing the elements of the networks.
        Each dictionary describes an element, and  specifies its purpose.
        The [official Cytoscape.js
        documentation](https://js.cytoscape.org/#notation/elements-json)
        offers an extensive overview and examples of element declaration.
        Alternatively, a dictionary with the format { 'nodes': [],
        'edges': [] } is allowed at initialization,  but arrays remain the
        recommended format.

        `elements` is a list of dicts with keys:

        - group (string; optional):
            Either 'nodes' or 'edges'. If not given, it's automatically
            inferred.

        - data (dict; optional):
            Element specific data.

            `data` is a dict with keys:

            - id (string; optional):
                Reference to the element, useful for selectors and edges.
                Randomly assigned if not given.

            - label (string; optional):
                Optional name for the element, useful when `data(label)`
                is given to a style's `content`  or `label`. It is only a
                convention.

            - parent (string; optional):
                Only for nodes. Optional reference to another node. Needed
                to create compound nodes.

            - source (string; optional):
                Only for edges. The id of the source node, which is where
                the edge starts.

            - target (string; optional):
                Only for edges. The id of the target node, where the edge
                ends.

        - position (dict; optional):
            Only for nodes. The position of the node.

            `position` is a dict with keys:

            - x (number; optional):
                The x-coordinate of the node.

            - y (number; optional):
                The y-coordinate of the node.

        - selected (boolean; optional):
            If the element is selected upon initialisation.

        - selectable (boolean; optional):
            If the element can be selected.

        - locked (boolean; optional):
            Only for nodes. If the position is immutable.

        - grabbable (boolean; optional):
            Only for nodes. If the node can be grabbed and moved by the
            user.

        - classes (string; optional):
            Space separated string of class names of the element. Those
            classes can be selected  by a style selector.

          Or dict with keys:

        - nodes (list; optional)

        - edges (list; optional)

    - extent (dict; optional):
        Extent of the viewport, a bounding box in model co-ordinates that
        lets you know what model  positions are visible in the viewport.
        This function returns a plain object bounding box  with format {
        x1, y1, x2, y2, w, h }.

    - generateImage (dict; optional):
        Dictionary specifying options to generate an image of the current
        cytoscape graph.  Value is cleared after data is received and
        image is generated. This property will  be ignored on the initial
        creation of the cytoscape object and must be invoked through  a
        callback after it has been rendered.    If the app does not need
        the image data server side and/or it will only be used to download
        the image, it may be prudent to invoke `'download'` for `action`
        instead of  `'store'` to improve performance by preventing
        transfer of data to the server.

        `generateImage` is a dict with keys:

        - type (a value equal to: 'svg', 'png', 'jpg', 'jpeg'; optional):
            File type to output.

        - options (dict; optional):
            Dictionary of options to cy.png() / cy.jpg() or cy.svg() for
            image generation.  See https://js.cytoscape.org/#core/export
            for details. For `'output'`, only 'base64'  and 'base64uri'
            are supported. Default: `{'output': 'base64uri'}`.

        - action (a value equal to: 'store', 'download', 'both'; optional):
            `'store'`: Stores the image data (only jpg and png are
            supported)  in `imageData` and invokes server-side Dash
            callbacks. `'download'`: Downloads the image  as a file with
            all data handling done client-side. No `imageData` callbacks
            are fired.  `'both'`: Stores image data and downloads image as
            file. The default is `'store'`.

        - filename (string; optional):
            Name for the file to be downloaded. Default: 'cyto'.

    - imageData (string; optional):
        String representation of the image requested with generateImage.
        Null if no  image was requested yet or the previous request
        failed. Read-only.

    - layout (dict; default {name: 'grid'}):
        A dictionary specifying how to set the position of the elements in
        your  graph. The `'name'` key is required, and indicates which
        layout (algorithm) to  use. The keys accepted by `layout` vary
        depending on the algorithm, but these  keys are accepted by all
        layouts: `fit`,  `padding`, `animate`, `animationDuration`,
        `boundingBox`.     The complete list of layouts and their accepted
        options are available on the   [Cytoscape.js
        docs](https://js.cytoscape.org/#layouts) . For the external
        layouts,  the options are listed in the \"API\" section of the
        README.   Note that certain keys are not supported in Dash since
        the value is a JavaScript   function or a callback. Please visit
        this  [issue](https://github.com/plotly/dash-cytoscape/issues/25)
        for more information.

        `layout` is a dict with keys:

        - name (a value equal to: 'random', 'preset', 'circle', 'concentric', 'grid', 'breadthfirst', 'cose', 'cose-bilkent', 'fcose', 'cola', 'euler', 'spread', 'dagre', 'klay'; required):
            The layouts available by default are:    `random`: Randomly
            assigns positions.    `preset`: Assigns position based on the
            `position` key in element dictionaries.    `circle`:
            Single-level circle, with optional radius.    `concentric`:
            Multi-level circle, with optional radius.    `grid`: Square
            grid, optionally with numbers of `rows` and `cols`.
            `breadthfirst`: Tree structure built using BFS, with optional
            `roots`.    `cose`: Force-directed physics simulation.    Some
            external layouts are also included. To use them, run
            `dash_cytoscape.load_extra_layouts()` before creating your
            Dash app. Be careful about    using the extra layouts when not
            necessary, since they require supplementary bandwidth    for
            loading, which impacts the startup time of the app.    The
            external layouts are:
            [cose-bilkent](https://github.com/cytoscape/cytoscape.js-cose-bilkent),
            [fcose](https://github.com/iVis-at-Bilkent/cytoscape.js-fcose),
            [cola](https://github.com/cytoscape/cytoscape.js-cola),
            [euler](https://github.com/cytoscape/cytoscape.js-dagre),
            [spread](https://github.com/cytoscape/cytoscape.js-spread),
            [dagre](https://github.com/cytoscape/cytoscape.js-dagre),
            [klay](https://github.com/cytoscape/cytoscape.js-klay),.

        - fit (boolean; optional):
            Whether to render the nodes in order to fit the canvas.

        - padding (number; optional):
            Padding around the sides of the canvas, if fit is enabled.

        - animate (boolean; optional):
            Whether to animate change in position when the layout changes.

        - animationDuration (number; optional):
            Duration of animation in milliseconds, if enabled.

        - boundingBox (dict; optional):
            How to constrain the layout in a specific area. Keys accepted
            are either  `x1, y1, x2, y2` or `x1, y1, w, h`, all of which
            receive a pixel value.

    - maxZoom (number; default 1e50):
        A maximum bound on the zoom level of the graph. The viewport can
        not be  scaled larger than this zoom level.

    - minZoom (number; default 1e-50):
        A minimum bound on the zoom level of the graph. The viewport can
        not be  scaled smaller than this zoom level.

    - mouseoverEdgeData (dict; optional):
        The data dictionary of an edge returned when you hover over it.
        Read-only.

    - mouseoverNodeData (dict; optional):
        The data dictionary of a node returned when you hover over it.
        Read-only.

    - pan (dict; default {x: 0, y: 0}):
        Dictionary indicating the initial panning position of the graph.
        The  following keys are accepted:.

        `pan` is a dict with keys:

        - x (number; optional):
            The x-coordinate of the node.

        - y (number; optional):
            The y-coordinate of the node.

    - panningEnabled (boolean; default True):
        Whether panning the graph is enabled (i.e., the position of the
        graph is  mutable overall).

    - responsive (boolean; default False):
        Toggles intelligent responsive resize of Cytoscape graph with
        viewport size change.

    - selectedEdgeData (list; optional):
        The list of data dictionaries of all selected edges (e.g. using
        Shift+Click to select multiple nodes, or Shift+Drag to use box
        selection). Read-only.

    - selectedNodeData (list; optional):
        The list of data dictionaries of all selected nodes (e.g. using
        Shift+Click to select multiple nodes, or Shift+Drag to use box
        selection). Read-only.

    - stylesheet (list of dicts; optional):
        A list of dictionaries representing the styles of the elements.
        Each dictionary requires the following keys: `selector` and
        `style`.    Both the
        [selector](https://js.cytoscape.org/#selectors) and  the
        [style](https://js.cytoscape.org/#style/node-body) are
        exhaustively documented in the Cytoscape.js docs. Although methods
        such  as `cy.elements(...)` and `cy.filter(...)` are not
        available, the selector  string syntax stays the same.

        `stylesheet` is a list of dicts with keys:

        - selector (string; required):
            Which elements you are styling. Generally, you select a group
            of elements (node, edges, both),  a class (that you declare in
            the element dictionary), or an element by ID.

        - style (dict; required):
            What aspects of the elements you want to modify. This could be
            the size or  color of a node, the shape of an edge arrow, or
            many more.

    - tapEdge (dict; optional):
        The complete edge dictionary returned when you tap or click it.
        Read-only.

        `tapEdge` is a dict with keys:

        - isLoop (boolean; optional):
            Edge-specific item.

        - isSimple (boolean; optional):
            Edge-specific item.

        - midpoint (dict; optional):
            Edge-specific item.

        - sourceData (dict; optional):
            Edge-specific item.

        - sourceEndpoint (dict; optional):
            Edge-specific item.

        - targetData (dict; optional):
            Edge-specific item.

        - targetEndpoint (dict; optional):
            Edge-specific item.

        - timeStamp (number; optional):
            Edge-specific item.

        - classes (string; optional):
            General item (for all elements).

        - data (dict; optional):
            General item (for all elements).

        - grabbable (boolean; optional):
            General item (for all elements).

        - group (string; optional):
            General item (for all elements).

        - locked (boolean; optional):
            General item (for all elements).

        - selectable (boolean; optional):
            General item (for all elements).

        - selected (boolean; optional):
            General item (for all elements).

        - style (dict; optional):
            General item (for all elements).

    - tapEdgeData (dict; optional):
        The data dictionary of an edge returned when you tap or click it.
        Read-only.

    - tapNode (dict; optional):
        The complete node dictionary returned when you tap or click it.
        Read-only.

        `tapNode` is a dict with keys:

        - edgesData (list; optional):
            node specific item.

        - renderedPosition (dict; optional):
            node specific item.

        - timeStamp (number; optional):
            node specific item.

        - classes (string; optional):
            General item (for all elements).

        - data (dict; optional):
            General item (for all elements).

        - grabbable (boolean; optional):
            General item (for all elements).

        - group (string; optional):
            General item (for all elements).

        - locked (boolean; optional):
            General item (for all elements).

        - position (dict; optional):
            General item (for all elements).

        - selectable (boolean; optional):
            General item (for all elements).

        - selected (boolean; optional):
            General item (for all elements).

        - style (dict; optional):
            General item (for all elements).

        - ancestorsData (dict | list; optional):
            Item for compound nodes.

        - childrenData (dict | list; optional):
            Item for compound nodes.

        - descendantsData (dict | list; optional):
            Item for compound nodes.

        - parentData (dict | list; optional):
            Item for compound nodes.

        - siblingsData (dict | list; optional):
            Item for compound nodes.

        - isParent (boolean; optional):
            Item for compound nodes.

        - isChildless (boolean; optional):
            Item for compound nodes.

        - isChild (boolean; optional):
            Item for compound nodes.

        - isOrphan (boolean; optional):
            Item for compound nodes.

        - relativePosition (dict; optional):
            Item for compound nodes.

    - tapNodeData (dict; optional):
        The data dictionary of a node returned when you tap or click it.
        Read-only.

    - userPanningEnabled (boolean; default True):
        Whether user events (e.g. dragging the graph background) are
        allowed to  pan the graph.

    - userZoomingEnabled (boolean; default True):
        Whether user events (e.g. dragging the graph background) are
        allowed  to pan the graph.

    - wheelSensitivity (number; default 1):
        Changes the scroll wheel sensitivity when zooming.

    - zoom (number; default 1):
        The initial zoom level of the graph. You can set `minZoom` and
        `maxZoom` to set restrictions on the zoom level.

    - zoomingEnabled (boolean; default True):
        Whether zooming the graph is enabled (i.e., the zoom level of the
        graph  is mutable overall)."""

    _children_props = []
    _base_nodes = ["children"]
    _namespace = "dash_cytoscape"
    _type = "Cytoscape"
    ElementsData = TypedDict(
        "ElementsData",
        {
            "id": NotRequired[str],
            "label": NotRequired[str],
            "parent": NotRequired[str],
            "source": NotRequired[str],
            "target": NotRequired[str],
        },
    )

    ElementsPosition = TypedDict(
        "ElementsPosition", {"x": NotRequired[NumberType], "y": NotRequired[NumberType]}
    )

    Elements = TypedDict(
        "Elements",
        {"nodes": NotRequired[typing.Sequence], "edges": NotRequired[typing.Sequence]},
    )

    Stylesheet = TypedDict("Stylesheet", {"selector": str, "style": dict})

    Layout = TypedDict(
        "Layout",
        {
            "name": Literal[
                "random",
                "preset",
                "circle",
                "concentric",
                "grid",
                "breadthfirst",
                "cose",
                "cose-bilkent",
                "fcose",
                "cola",
                "euler",
                "spread",
                "dagre",
                "klay",
            ],
            "fit": NotRequired[bool],
            "padding": NotRequired[NumberType],
            "animate": NotRequired[bool],
            "animationDuration": NotRequired[NumberType],
            "boundingBox": NotRequired[dict],
        },
    )

    ContextMenu = TypedDict(
        "ContextMenu",
        {
            "id": str,
            "label": str,
            "tooltipText": NotRequired[str],
            "availableOn": NotRequired[typing.Sequence],
            "onClick": NotRequired[str],
            "onClickCustom": NotRequired[str],
        },
    )

    ContextMenuData = TypedDict(
        "ContextMenuData",
        {
            "menuItemId": NotRequired[str],
            "x": NotRequired[NumberType],
            "y": NotRequired[NumberType],
            "timeStamp": NotRequired[NumberType],
            "elementId": NotRequired[str],
            "edgeSource": NotRequired[str],
            "edgeTarget": NotRequired[str],
        },
    )

    Pan = TypedDict("Pan", {"x": NotRequired[NumberType], "y": NotRequired[NumberType]})

    TapNode = TypedDict(
        "TapNode",
        {
            "edgesData": NotRequired[typing.Sequence],
            "renderedPosition": NotRequired[dict],
            "timeStamp": NotRequired[NumberType],
            "classes": NotRequired[str],
            "data": NotRequired[dict],
            "grabbable": NotRequired[bool],
            "group": NotRequired[str],
            "locked": NotRequired[bool],
            "position": NotRequired[dict],
            "selectable": NotRequired[bool],
            "selected": NotRequired[bool],
            "style": NotRequired[dict],
            "ancestorsData": NotRequired[typing.Union[dict, typing.Sequence]],
            "childrenData": NotRequired[typing.Union[dict, typing.Sequence]],
            "descendantsData": NotRequired[typing.Union[dict, typing.Sequence]],
            "parentData": NotRequired[typing.Union[dict, typing.Sequence]],
            "siblingsData": NotRequired[typing.Union[dict, typing.Sequence]],
            "isParent": NotRequired[bool],
            "isChildless": NotRequired[bool],
            "isChild": NotRequired[bool],
            "isOrphan": NotRequired[bool],
            "relativePosition": NotRequired[dict],
        },
    )

    TapEdge = TypedDict(
        "TapEdge",
        {
            "isLoop": NotRequired[bool],
            "isSimple": NotRequired[bool],
            "midpoint": NotRequired[dict],
            "sourceData": NotRequired[dict],
            "sourceEndpoint": NotRequired[dict],
            "targetData": NotRequired[dict],
            "targetEndpoint": NotRequired[dict],
            "timeStamp": NotRequired[NumberType],
            "classes": NotRequired[str],
            "data": NotRequired[dict],
            "grabbable": NotRequired[bool],
            "group": NotRequired[str],
            "locked": NotRequired[bool],
            "selectable": NotRequired[bool],
            "selected": NotRequired[bool],
            "style": NotRequired[dict],
        },
    )

    GenerateImage = TypedDict(
        "GenerateImage",
        {
            "type": NotRequired[Literal["svg", "png", "jpg", "jpeg"]],
            "options": NotRequired[dict],
            "action": NotRequired[Literal["store", "download", "both"]],
            "filename": NotRequired[str],
        },
    )

    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        elements: typing.Optional[
            typing.Union[typing.Sequence["Elements"], "Elements"]
        ] = None,
        stylesheet: typing.Optional[typing.Sequence["Stylesheet"]] = None,
        layout: typing.Optional["Layout"] = None,
        contextMenu: typing.Optional[typing.Sequence["ContextMenu"]] = None,
        contextMenuData: typing.Optional["ContextMenuData"] = None,
        pan: typing.Optional["Pan"] = None,
        zoom: typing.Optional[NumberType] = None,
        panningEnabled: typing.Optional[bool] = None,
        userPanningEnabled: typing.Optional[bool] = None,
        minZoom: typing.Optional[NumberType] = None,
        maxZoom: typing.Optional[NumberType] = None,
        zoomingEnabled: typing.Optional[bool] = None,
        userZoomingEnabled: typing.Optional[bool] = None,
        wheelSensitivity: typing.Optional[NumberType] = None,
        boxSelectionEnabled: typing.Optional[bool] = None,
        autoungrabify: typing.Optional[bool] = None,
        autolock: typing.Optional[bool] = None,
        autounselectify: typing.Optional[bool] = None,
        autoRefreshLayout: typing.Optional[bool] = None,
        tapNode: typing.Optional["TapNode"] = None,
        tapNodeData: typing.Optional[dict] = None,
        tapEdge: typing.Optional["TapEdge"] = None,
        tapEdgeData: typing.Optional[dict] = None,
        mouseoverNodeData: typing.Optional[dict] = None,
        mouseoverEdgeData: typing.Optional[dict] = None,
        selectedNodeData: typing.Optional[typing.Sequence] = None,
        selectedEdgeData: typing.Optional[typing.Sequence] = None,
        generateImage: typing.Optional["GenerateImage"] = None,
        imageData: typing.Optional[str] = None,
        responsive: typing.Optional[bool] = None,
        extent: typing.Optional[dict] = None,
        clearOnUnhover: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = [
            "id",
            "autoRefreshLayout",
            "autolock",
            "autoungrabify",
            "autounselectify",
            "boxSelectionEnabled",
            "className",
            "clearOnUnhover",
            "contextMenu",
            "contextMenuData",
            "elements",
            "extent",
            "generateImage",
            "imageData",
            "layout",
            "maxZoom",
            "minZoom",
            "mouseoverEdgeData",
            "mouseoverNodeData",
            "pan",
            "panningEnabled",
            "responsive",
            "selectedEdgeData",
            "selectedNodeData",
            "style",
            "stylesheet",
            "tapEdge",
            "tapEdgeData",
            "tapNode",
            "tapNodeData",
            "userPanningEnabled",
            "userZoomingEnabled",
            "wheelSensitivity",
            "zoom",
            "zoomingEnabled",
        ]
        self._valid_wildcard_attributes = []
        self.available_properties = [
            "id",
            "autoRefreshLayout",
            "autolock",
            "autoungrabify",
            "autounselectify",
            "boxSelectionEnabled",
            "className",
            "clearOnUnhover",
            "contextMenu",
            "contextMenuData",
            "elements",
            "extent",
            "generateImage",
            "imageData",
            "layout",
            "maxZoom",
            "minZoom",
            "mouseoverEdgeData",
            "mouseoverNodeData",
            "pan",
            "panningEnabled",
            "responsive",
            "selectedEdgeData",
            "selectedNodeData",
            "style",
            "stylesheet",
            "tapEdge",
            "tapEdgeData",
            "tapNode",
            "tapNodeData",
            "userPanningEnabled",
            "userZoomingEnabled",
            "wheelSensitivity",
            "zoom",
            "zoomingEnabled",
        ]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Cytoscape, self).__init__(**args)


setattr(Cytoscape, "__init__", _explicitize_args(Cytoscape.__init__))
