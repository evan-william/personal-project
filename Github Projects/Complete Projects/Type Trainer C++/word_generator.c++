#include <iostream>
#include <cstdlib>  // for rand()
#include <ctime>    // for time()
#include <vector>
#include "word_generator.h"

using namespace std;

string generate_word() {

    static vector<string> word_list = {
    "i", "hate", "rain", "sun", "love", "peace", "fire", "storm", 
    "moon", "star", "robot", "magic", "dream", "code", "light", 
    "shadow", "dragon", "music", "banana", "zebra", "forest", "river", 
    "mountain", "galaxy", "cloud", "wind", "ocean", "planet", "alien", 
    "future", "past", "portal", "castle", "knight", "sword", "wizard", 
    "beast", "ghost", "spirit", "night", "day", "truth", "fear", "hope", 
    "chaos", "order", "space", "time", "energy", "spark", "flame", "ice", 
    "thunder", "crystal", "mirror", "illusion", "monster", "game", "power", 
    "quest", "hero", "villain", "sky", "earth", "core", "machine", "signal", 
    "data", "glitch", "virus", "command", "debug", "syntax", "logic", "array", 
    "vector", "pixel", "input", "output", "buffer", "loop", "frame", "thread", 
    "server", "client", "dimension", "network", "lightning", "stormy", "breeze", 
    "tempest", "cloudy", "sunshine", "moonlight", "dawn", "twilight", "sunset", 
    "starry", "comet", "eclipse", "nebula", "orbit", "galactic", "explosion", 
    "blackhole", "gravity", "force", "velocity", "quantum", "nucleus", "atom", 
    "electron", "proton", "neutron", "fusion", "fission", "energy", "radiation", 
    "magnetism", "charge", "electricity", "current", "voltage", "resistance", 
    "conductor", "insulator", "circuit", "ampere", "joule", "ohm", "watt", "photon", 
    "laser", "microwave", "fiber", "wireless", "satellite", "telecommunication", 
    "internet", "server", "network", "wifi", "bluetooth", "router", "cloud", 
    "data", "server", "upload", "download", "website", "browser", "search", 
    "engine", "link", "html", "css", "javascript", "python", "java", "ruby", "swift", 
    "csharp", "cpp", "cplusplus", "database", "sql", "nosql", "mongodb", "mysql", 
    "postgresql", "sqlite", "api", "endpoint", "authentication", "authorization", 
    "session", "token", "cookie", "request", "response", "url", "uri", "rest", 
    "graphql", "method", "get", "post", "put", "delete", "patch", "client", 
    "server", "message", "protocol", "https", "http", "smtp", "ftp", "ssh", "tls", 
    "ssl", "encryption", "hashing", "signature", "key", "salt", "cipher", 
    "decryption", "compression", "protocol", "communication", "ip", "port", "dns", 
    "proxy", "vpn", "firewall", "router", "packet", "switch", "bridge", "subnet", 
    "gateway", "broadcast", "multicast", "unicast", "networking", "topology", 
    "routing", "forwarding", "address", "mac", "ipv4", "ipv6", "subnetmask", 
    "networkaddress", "broadcastaddress", "gatewayaddress", "dhcp", "dhcpserver", 
    "host", "hostname", "domain", "dnsserver", "proxyserver", "tftp", "icmp", 
    "ping", "traceroute", "tracepath", "ipconfig", "ifconfig", "netstat", "pinging", 
    "latency", "jitter", "throughput", "packetloss", "bandwidth", "loadbalancer", 
    "multithreading", "asynchronous", "concurrency", "parallel", "sync", "async", 
    "mutex", "lock", "thread", "process", "deadlock", "racecondition", "threadpool", 
    "semaphore", "queue", "stack", "priorityqueue", "deque", "linkedlist", "array", 
    "hashmap", "dictionary", "hashset", "list", "iterator", "pointer", "reference", 
    "null", "nullptr", "memory", "garbage", "allocator", "new", "delete", "free", 
    "malloc", "calloc", "realloc", "memcpy", "memmove", "strcmp", "strcpy", 
    "strcat", "strlen", "file", "filesystem", "stream", "inputstream", "outputstream", 
    "fstream", "ifstream", "ofstream", "filehandler", "write", "read", "flush", 
    "seek", "open", "close", "mkdir", "rmdir", "remove", "rename", "stat", "chmod", 
    "chown", "touch", "fileexists", "path", "basename", "dirname", "extension", 
    "filename", "direntry", "syscall", "error", "exception", "throw", "catch", 
    "try", "finally", "assert", "debug", "log", "logging", "tracing", "trace", 
    "debugger", "breakpoint", "watch", "step", "stacktrace", "callstack", "dump", 
    "assertion", "assertfailure", "test", "unit", "integration", "system", 
    "acceptance", "testing", "testcase", "mock", "stub", "assert", "errorhandling", 
    "assertionerror", "debugging", "bug", "fix", "refactor", "optimizing", "performance", 
    "codequality", "codecoverage", "unitest", "mockito", "jest", "pytest", "mocha", 
    "ci", "cd", "build", "pipeline", "jenkins", "docker", "kubernetes", "terraform", 
    "ansible", "cloudformation", "deploy", "devops", "agile", "scrum", "kanban", 
    "sprint", "userstory", "task", "backlog", "jira", "trello", "slack", "teams", 
    "confluence", "notion", "todo", "planning", "milestone", "calendar", "meeting", 
    "presentation", "conference", "workshop", "seminar", "webinar", "networking", 
    "leadership", "management", "project", "plan", "schedule", "budget", "timeline", 
    "goal", "objective", "strategy", "tactics", "execution", "scope", "risk", 
    "issue", "resource", "stakeholder", "client", "team", "collaboration", 
    "communication", "negotiation", "decision", "problem", "solution", "innovation", 
    "growth", "success", "failure", "learning", "improvement", "feedback", 
    "performance", "evaluation", "review", "training", "development", "coaching", 
    "mentoring", "leadership", "teamwork", "culture", "vision", "mission"
};

    int random_word_picker = rand() % word_list.size();

    return word_list[random_word_picker];
}