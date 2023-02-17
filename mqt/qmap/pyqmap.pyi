from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, overload

if TYPE_CHECKING:  # pragma: no cover
    from qiskit import QuantumCircuit

class Arch:
    __members__: ClassVar[dict[Arch, int]] = ...  # read-only
    IBMQ_Bogota: ClassVar[Arch] = ...
    IBMQ_Casablanca: ClassVar[Arch] = ...
    IBMQ_London: ClassVar[Arch] = ...
    IBMQ_Tokyo: ClassVar[Arch] = ...
    IBMQ_Yorktown: ClassVar[Arch] = ...
    IBM_QX4: ClassVar[Arch] = ...
    IBM_QX5: ClassVar[Arch] = ...
    Rigetti_Agave: ClassVar[Arch] = ...
    Rigetti_Aspen: ClassVar[Arch] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Architecture:
    class Properties:
        name: str
        num_qubits: int
        def __init__(self) -> None: ...
        def get_calibration_date(self, qubit: int) -> str: ...
        def get_frequency(self, qubit: int) -> float: ...
        def get_readout_error(self, qubit: int) -> float: ...
        def get_single_qubit_error(self, qubit: int, operation: str) -> float: ...
        def get_t1(self, qubit: int) -> float: ...
        def get_t2(self, qubit: int) -> float: ...
        def get_two_qubit_error(self, control: int, target: int, operation: str = ...) -> float: ...
        def json(self) -> dict[str, Any]: ...
        def set_calibration_date(self, qubit: int, calibration_date: str) -> None: ...
        def set_frequency(self, qubit: int, qubit_frequency: float) -> None: ...
        def set_readout_error(self, qubit: int, readout_error_rate: float) -> None: ...
        def set_single_qubit_error(self, qubit: int, operation: str, error_rate: float) -> None: ...
        def set_t1(self, qubit: int, t1: float) -> None: ...
        def set_t2(self, qubit: int, t2: float) -> None: ...
        def set_two_qubit_error(self, control: int, target: int, error_rate: float, operation: str = ...) -> None: ...
    coupling_map: set[tuple[int, int]]
    name: str
    num_qubits: int
    properties: Architecture.Properties
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, num_qubits: int, coupling_map: set[tuple[int, int]]) -> None: ...
    @overload
    def __init__(
        self, num_qubits: int, coupling_map: set[tuple[int, int]], properties: Architecture.Properties
    ) -> None: ...
    @overload
    def load_coupling_map(self, available_architecture: Arch) -> None: ...
    @overload
    def load_coupling_map(self, coupling_map_file: str) -> None: ...
    @overload
    def load_properties(self, properties: Architecture.Properties) -> None: ...
    @overload
    def load_properties(self, properties: str) -> None: ...

class CircuitInfo:
    cnots: int
    direction_reverse: int
    gates: int
    layers: int
    name: str
    qubits: int
    single_qubit_gates: int
    swaps: int
    teleportations: int
    def __init__(self) -> None: ...

class CommanderGrouping:
    __members__: ClassVar[dict[CommanderGrouping, int]] = ...  # read-only
    fixed2: ClassVar[CommanderGrouping] = ...
    fixed3: ClassVar[CommanderGrouping] = ...
    halves: ClassVar[CommanderGrouping] = ...
    logarithm: ClassVar[CommanderGrouping] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: CommanderGrouping) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Configuration:
    add_measurements_to_mapped_circuit: bool
    admissible_heuristic: bool
    consider_fidelity: bool
    commander_grouping: CommanderGrouping
    enable_limits: bool
    encoding: Encoding
    first_lookahead_factor: float
    include_WCNF: bool  # noqa: N815
    initial_layout: InitialLayout
    layering: Layering
    lookahead: bool
    lookahead_factor: float
    lookaheads: int
    method: Method
    post_mapping_optimizations: bool
    pre_mapping_optimizations: bool
    subgraph: set[int]
    swap_limit: int
    swap_reduction: SwapReduction
    teleportation_fake: bool
    teleportation_qubits: int
    teleportation_seed: int
    timeout: int
    use_bdd: bool
    use_subsets: bool
    use_teleportation: bool
    verbose: bool
    def __init__(self) -> None: ...
    def json(self) -> dict[str, Any]: ...

class Encoding:
    __members__: ClassVar[dict[Encoding, int]] = ...  # read-only
    bimander: ClassVar[Encoding] = ...
    commander: ClassVar[Encoding] = ...
    naive: ClassVar[Encoding] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: Encoding) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class InitialLayout:
    __members__: ClassVar[dict[InitialLayout, int]] = ...  # read-only
    dynamic: ClassVar[InitialLayout] = ...
    identity: ClassVar[InitialLayout] = ...
    static: ClassVar[InitialLayout] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: InitialLayout) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Layering:
    __members__: ClassVar[dict[Layering, int]] = ...  # read-only
    disjoint_qubits: ClassVar[Layering] = ...
    individual_gates: ClassVar[Layering] = ...
    odd_gates: ClassVar[Layering] = ...
    qubit_triangle: ClassVar[Layering] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: Layering) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MappingResults:
    configuration: Configuration
    input: Any  # noqa: A003
    mapped_circuit: str
    output: Any
    time: float
    timeout: bool
    wcnf: str
    def __init__(self) -> None: ...
    def csv(self) -> str: ...
    def json(self) -> dict[str, Any]: ...

class Method:
    __members__: ClassVar[dict[Method, int]] = ...  # read-only
    exact: ClassVar[Method] = ...
    heuristic: ClassVar[Method] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: Method) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SwapReduction:
    __members__: ClassVar[dict[SwapReduction, int]] = ...  # read-only
    coupling_limit: ClassVar[SwapReduction] = ...
    custom: ClassVar[SwapReduction] = ...
    increasing: ClassVar[SwapReduction] = ...
    none: ClassVar[SwapReduction] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: SwapReduction) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def map(circ: str | QuantumCircuit, arch: Architecture, config: Configuration) -> MappingResults: ...  # noqa: A001

class TargetMetric:
    __members__: ClassVar[dict[TargetMetric, int]] = ...  # read-only
    depth: ClassVar[TargetMetric] = ...
    gates: ClassVar[TargetMetric] = ...
    two_qubit_gates: ClassVar[TargetMetric] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: TargetMetric) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Verbosity:
    __members__: ClassVar[dict[Verbosity, int]] = ...  # read-only
    none: ClassVar[Verbosity] = ...
    fatal: ClassVar[Verbosity] = ...
    error: ClassVar[Verbosity] = ...
    warning: ClassVar[Verbosity] = ...
    info: ClassVar[Verbosity] = ...
    debug: ClassVar[Verbosity] = ...
    verbose: ClassVar[Verbosity] = ...
    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: Verbosity) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SynthesisConfiguration:
    dump_intermediate_results: bool
    gate_limit_factor: float
    initial_timestep_limit: int
    intermediate_results_path: str
    minimize_gates_after_depth_optimization: bool
    minimize_gates_after_two_qubit_gate_optimization: bool
    n_threads: int
    target_metric: TargetMetric
    try_higher_gate_limit_for_two_qubit_gate_optimization: bool
    use_maxsat: bool
    use_symmetry_breaking: bool
    verbosity: Verbosity
    def __init__(self) -> None: ...
    def json(self) -> dict[str, Any]: ...

class SynthesisResults:
    def __init__(self) -> None: ...
    def sat(self) -> bool: ...
    def unsat(self) -> bool: ...
    @property
    def circuit(self) -> str: ...
    @property
    def depth(self) -> int: ...
    @property
    def gates(self) -> int: ...
    @property
    def runtime(self) -> float: ...
    @property
    def single_qubit_gates(self) -> int: ...
    @property
    def solver_calls(self) -> int: ...
    @property
    def tableau(self) -> str: ...
    @property
    def two_qubit_gates(self) -> int: ...

class QuantumComputation:
    def __init__(self) -> None: ...
    @staticmethod
    def from_file(file: str) -> QuantumComputation: ...
    @staticmethod
    def from_qasm_str(qasm: str) -> QuantumComputation: ...
    @staticmethod
    def from_qiskit(circuit: QuantumCircuit) -> QuantumComputation: ...

class Tableau:
    @overload
    def __init__(self, n: int) -> None: ...
    @overload
    def __init__(self, description: str) -> None: ...

class CliffordSynthesizer:
    @overload
    def __init__(self, initial_tableau: Tableau, target_tableau: Tableau) -> None: ...
    @overload
    def __init__(self, target_tableau: Tableau) -> None: ...
    @overload
    def __init__(self, qc: QuantumComputation) -> None: ...
    @overload
    def __init__(self, initial_tableau: Tableau, qc: QuantumComputation) -> None: ...
    def synthesize(self, config: SynthesisConfiguration = ...) -> None: ...
    @property
    def results(self) -> SynthesisResults: ...
