//
// This file is part of the MQT QMAP library released under the MIT license.
// See README.md or go to https://github.com/cda-tum/qmap for more information.
//

#pragma once

#include "Definitions.hpp"
#include "operations/OpType.hpp"

#include <cstdint>
#include <cstdlib>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace na {

/**
 * @brief The scope of an operation (Global or Local)
 */
enum class Scope { Global, Local };
static std::map<std::string, Scope> const STRING_TO_SCOPE = {
    {"Global", Scope::Global}, {"Local", Scope::Local}};
/**
 * @brief Get the Scope of a gate from a string
 *
 * @param s the name
 * @return Type
 */
inline Scope getScopeOfString(const std::string& s) {
  auto it = STRING_TO_SCOPE.find(s);
  return it->second;
}

/**
 * @brief The type of a site (SLM or AOD)
 * @details SLM comprises both AOD and SLM; AOD denotes AOD only.
 */
enum class Type { SLM, AOD };
static std::map<std::string, Type> const STRING_TO_TYPE = {{"SLM", Type::SLM},
                                                           {"AOD", Type::AOD}};
/**
 * @brief Get the Type of a site (SLM or AOD) from a string
 *
 * @param s the name
 * @return Type
 */
inline Type getTypeOfString(const std::string& s) {
  auto it = STRING_TO_TYPE.find(s);
  return it->second;
}

/**
 * @brief Class to store two-dimensional coordinates
 */
class Point {
public:
  std::uint16_t x;
  std::uint16_t y;
  Point(std::uint16_t x, std::uint16_t y) : x(x), y(y){};
  inline Point operator-(const Point&& p) {
    x -= p.x;
    y -= p.y;
    return *this;
  }
  inline Point operator+(const Point&& p) {
    x += p.x;
    y += p.y;
    return *this;
  }
  [[nodiscard]] auto length() const { return std::abs(x * x + y * y); }
};

/**
 * @brief For Indices
 */
using Index = std::size_t;
/**
 * @brief The zones are just stored as int
 */
using Zone = Index;
/**
 * @brief A site is defined by a position, a zone, and a type
 */
using Site = std::tuple<Point, Zone, Type>;
/**
 * @brief Any double-valued property
 */
using Value = qc::fp;
/**
 * @brief Any information on numbers of somethin
 */
using Number = std::uint16_t;

class Architecture {
public:
  /**
   * @brief Class to store the decoherence times of a neutral atom
   * architecture
   * @details
   * The decoherence times of a neutral atom architecture are:
   * - T1
   * - T2
   * - effective decoherence time
   */
  class DecoherenceTimes {
  public:
    Value t1                              = 0;
    Value t2                              = 0;
    Value tEff                            = 0;
    DecoherenceTimes()                    = default;
    DecoherenceTimes(DecoherenceTimes& t) = default;
    inline DecoherenceTimes(Value t1, Value t2)
        : t1(t1), t2(t2), tEff(t1 * t2 / (t1 + t2)) {}
    virtual ~DecoherenceTimes() = default;
    explicit          operator double() const { return tEff; }
    DecoherenceTimes& operator=(DecoherenceTimes&& t) noexcept {
      if (this != &t) {
        t1   = t.t1;
        t2   = t.t2;
        tEff = t.tEff;
      }
      return *this;
    }
  };
  class Operation {
  public:
    qc::OpType type;  // the type of the gate, use also RY for global ones here
    Scope      scope; // local or global
    std::set<Zone> zones;    // the zones where the gate can be applied
    Value          time;     // the time the gate takes to be applied
    Value          fidelity; // the fidelity of the gate
    Operation(const Operation& op) = default;
    Operation(qc::OpType type, Scope scope, std::set<Zone> zones, Value time,
              Value fidelity)
        : type(type), scope(scope), zones(std::move(zones)), time(time),
          fidelity(fidelity) {}
  };

protected:
  std::string name; // the name of the architecure
  std::vector<std::string>
      zones; // a mapping from zones (int) to their name from the config
  std::vector<Site> sites;  // a vector of sites (Position, Zone, Type)
  Number            nSites; // number of sites
  std::map<qc::OpType, Operation>
                   operations; // all possible operations by their type, i.e. gate set
  DecoherenceTimes decoherenceTimes; // the decoherence characteristic
  Number           nAods;            // number of AODs for atom movement
  Number           nAodRows;         // possible rows per AOD
  Number           nAodCols;         // possible columns per AOD
  Value minAtomDistance;   // minimal distance that must be kept between atoms
  Value interactionRadius; // the Rydberg radius

public:
  /**
   * @brief Import a new architecture from a file.
   *
   * @param filename The path to the JSON file
   */
  explicit Architecture(std::string& filename);
  virtual ~Architecture() = default;
  [[nodiscard]] inline auto getName() { return name; }
  [[nodiscard]] inline auto getNZones() { return zones.size(); }
  [[nodiscard]] inline auto getZoneLabel(const Index& i) { return zones.at(i); }
  [[nodiscard]] inline auto getNSites() const { return nSites; }
  [[nodiscard]] auto        getType(const Index& i) {
    return std::get<Type>(sites.at(i));
  }
  [[nodiscard]] auto getZone(const Index& i) {
    return std::get<Zone>(sites.at(i));
  }
  [[nodiscard]] inline auto getPos(const Index& i) {
    return std::get<Point>(sites.at(i));
  }
  [[nodiscard]] inline auto getDecoherenceTimes() { return decoherenceTimes; }
  [[nodiscard]] inline auto getNAods() const { return nAods; }
  [[nodiscard]] inline auto getNAodRows() const { return nAodRows; }
  [[nodiscard]] inline auto getNAodCols() const { return nAodCols; }
  [[nodiscard]] inline auto getMinAtomDistance() const { return minAtomDistance; }
  [[nodiscard]] inline auto getInteractionRadius() const { return interactionRadius; }
  [[nodiscard]] auto        getOperationByOpType(const qc::OpType& t) {
    auto it = operations.find(t);
    if (it == operations.end()) {
      throw std::invalid_argument(
          "This operation is not supported by this architecure.");
    }
    return it->second;
  }
  [[nodiscard]] auto getDistance(Index i, Index j) {
    return (getPos(j) - getPos(i)).length();
  }
};
} // namespace na
